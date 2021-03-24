#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from mavros_msgs.srv import CommandBool

def arm_client(is_armed):
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        # command.base_mode = base_mode
        # command.custom_mode = custom_mode
        arm = rospy.ServiceProxy('/mavros/cmd/arming', CommandBool)
        resp1 = arm(is_armed)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        is_armed = bool(sys.argv[1])
    else:
        is_armed = True
    print("Requesting to arm the drone...")
    print("Armed = ", arm_client(is_armed))