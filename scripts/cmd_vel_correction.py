#!/usr/bin/env python

import math
import rospy

from geometry_msgs.msg import Twist
pub = None

global_tz = 0

def record_vel(msg):
    global global_tz
    global_tz += msg.angular.z*0.1 #assuming rate = 10Hz
    vx = msg.linear.x
    vz = msg.linear.z
    wz = msg.angular.z
    
    make_correction(vx, vz, wz)
    
def make_correction(given_vx, given_vz, given_wz):
    global global_tz
    msg = Twist()
    correct_vx = given_vx*math.cos(global_tz)
    correct_vy = given_vx*math.sin(global_tz)

    rospy.loginfo("given(vx, wz):", given_vx, given_wz)
    rospy.loginfo("corrected(vx, vy):", correct_vx, correct_vy)
    msg.linear.x = correct_vx
    msg.linear.y = correct_vy
    msg.linear.z = given_vz
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = given_wz
    pub.publish(msg)

def main():
    global pub
    
    rospy.init_node('cmd_vel_correction')
    
    pub = rospy.Publisher('/mavros/setpoint_velocity/cmd_vel_unstamped', Twist, queue_size=1)
    
    sub = rospy.Subscriber('/cmd_vel', Twist, record_vel)
    
    rospy.spin()

if __name__ == '__main__':
    main()
