#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from mavros_msgs.srv import SetMode

def set_mode_client(base_mode, custom_mode):
    rospy.wait_for_service('/mavros/set_mode')
    try:
        # command.base_mode = base_mode
        # command.custom_mode = custom_mode
        set_mode = rospy.ServiceProxy('/mavros/set_mode', SetMode)
        resp1 = set_mode(base_mode, custom_mode)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        base_mode = int(sys.argv[1])
        custom_mode = sys.argv[2]
    if len(sys.argv) == 2:
        custom_mode = sys.argv[1]
    else:
        base_mode = 0
        custom_mode = "GUIDED"
    print("Requesting set_mode", base_mode, "and custom_mode", custom_mode)
    print("Set mode = ", set_mode_client(base_mode, custom_mode))