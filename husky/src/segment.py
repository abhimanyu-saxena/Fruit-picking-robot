import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np

bridge = CvBridge()

def image_callback(img_msg):
    # log some info about the image topic
    rospy.loginfo(img_msg.data)

    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
        blur = cv2.blur(np.float32(cv_image.data), (10,10))
        img_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        lower_red = np.array([160,50,50])
        upper_red = np.array([180,255,255])  
        mask = cv2.inRange(img_hsv, lower_red, upper_red)
        res = cv2.bitwise_and(blur,blur, mask= mask)
        segmsg = bridge.cv2_to_imgmsg(res, "bgr8")
        rospy.init_node('image_output', anonymous=True)
        pub = rospy.Publisher('/segmented_image', Image, queue_size=10)
        pub.publish(segmsg)
    except CvBridgeError:
        rospy.logerr("CvBridge Error")

def subpub():
    rospy.init_node('image_input', anonymous=True)
    rospy.Subscriber('/image_raw', Image, image_callback)
    # blur = cv2.blur(np.float32(orig), (10,10))
    # img_hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # lower_red = np.array([160,50,50])
    # upper_red = np.array([180,255,255])  
    # mask = cv2.inRange(img_hsv, lower_red, upper_red)
    # res = cv2.bitwise_and(blur,blur, mask= mask)
    # segmsg = bridge.cv2_to_imgmsg(res, "bgr8")
    # rospy.init_node('image_output', anonymous=True)
    # pub = rospy.Publisher('/segmented_image', Image, queue_size=10)
    # pub.publish(segmsg)
    rospy.spin()

if __name__ == '__main__':
    try:
        subpub()
    except rospy.ROSInterruptException:
        pass






