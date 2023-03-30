#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64

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
        state = int(input("Enter state:"))
        if state == 1:
            input_angles(home)
            rate.sleep()
        elif state == 2:
            input_angles(pick)
            rate.sleep()
        elif state == 3:
            input_angles(place)
            rate.sleep()
        else:
            break

if __name__ == '__main__':
    print("Menu:\n\t1: Home state\n\t2: Pick pose\n\t3: Place state\n\t 0: Exit")
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
