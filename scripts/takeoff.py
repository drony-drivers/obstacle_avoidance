#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from mavros_msgs.srv import CommandTOL


def takeoff_client(min_pitch, yaw, latitude, longitude, altitude):
    service_name = "/mavros/cmd/takeoff"
    rospy.wait_for_service(service_name)
    try:
        set_armed = rospy.ServiceProxy(service_name, CommandTOL)
        resp1 = set_armed(min_pitch, yaw, latitude, longitude, altitude)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        exit(1)

if __name__ == "__main__":
    min_pitch = 0
    yaw = 0
    latitude = 0
    longitude = 0
    if len(sys.argv) == 6:
        min_pitch = float(sys.argv[1])
        yaw = float(sys.argv[2])
        latitude = float(sys.argv[3])
        longitude = float(sys.argv[4])
        altitude = float(sys.argv[5])
    elif len(sys.argv) == 2:
        altitude = float(sys.argv[1])
    else:
        altitude = 2
    print("Requesting to takeoff...")
    print("Takeoff =", takeoff_client(min_pitch, yaw, latitude, longitude, altitude))