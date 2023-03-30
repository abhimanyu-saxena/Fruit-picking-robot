#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import numpy as np

spawn = [0,0,0]
home = [0.5,-0.1,-1.0]
pick = [0.5,-0.1,-0.5]
place = [-0.5,-0.1,2.5]


pub_joint2_position = rospy.Publisher('/husky/joint2_position_controller/command', Float64, queue_size=10)
pub_joint3_position = rospy.Publisher('/husky/joint3_position_controller/command', Float64, queue_size=10)
pub_joint4_position = rospy.Publisher('/husky/joint4_position_controller/command', Float64, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10)

def input_angles(st):
    rospy.loginfo(st[0])
    pub_joint2_position.publish(st[0])
    rospy.loginfo(st[1])
    pub_joint3_position.publish(st[1])
    rospy.loginfo(st[2])
    pub_joint4_position.publish(st[2])


def talker():
 # 10hz
    while not rospy.is_shutdown():
        ja2 = np.radians(float(input("Enter joint angle 2:")))
        ja3 = np.radians(float(input("Enter joint angle 3:")))
        ja4 = np.radians(float(input("Enter joint angle 4:")))
        input_angles([ja2,ja3,ja4])
        


if __name__ == '__main__':
    print("Validate Forward Kinematics:\n")
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
