#!/usr/bin/env python

##Husky Script Publisher

import rospy
from std_msgs.msg import Float64

 # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'

# rospy.init_node('talker', anonymous=True)

def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

def talker():
    rospy.init_node('talker', anonymous=True)
    # Save current time and set publish rate at 10 Hz
    # Create a publisher which can "talk" to husky Robot and tell it to move
    pub_right = rospy.Publisher('/husky/Front_R_lateral_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_left = rospy.Publisher('/husky/Front_L_lateral_controller/command', Float64, queue_size=10)
    pub_moveL = rospy.Publisher('/husky/wheel_BL_controller/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
    pub_moveR = rospy.Publisher('/husky/wheel_BR_controller/command', Float64, queue_size=10)
    now = rospy.Time.now()
    rate = rospy.Rate(10)
    speed = Float64()
    turn = Float64()




    # For the next 30 seconds publish turn&speed commands to Robot
    #while rospy.Time.now() < now + rospy.Duration.from_sec(60):
    while not rospy.is_shutdown():
        speed.data = 8.0
        turn.data = 0.5
        pub_moveL.publish(speed)
        pub_moveR.publish(speed)
        pub_left.publish(turn)
        pub_right.publish(turn)
        print (vels(speed.data,turn.data))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
