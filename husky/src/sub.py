#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'listening: %s', data.data)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/husky/Front_L_lateral_controller/command', Float64, callback)
    rospy.Subscriber('/husky/Front_R_lateral_controller/command', Float64, callback)
    rospy.Subscriber('/husky/wheel_BL_controller/command', Float64, callback)
    rospy.Subscriber('/husky/wheel_BR_controller/command', Float64, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()