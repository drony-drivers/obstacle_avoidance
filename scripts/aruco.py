#!/usr/bin/env python

from __future__ import print_function

# rospy for the subscriber
import rospy
from std_msgs.msg import String
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import imutils
import subprocess
import sys

bridge = CvBridge()
sub = None
pub = None

def image_callback(msg):
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    else:
        image = cv2_img
        image = imutils.resize(image, width=600)
        # loop over the types of ArUco dictionaries
        # load the ArUCo dictionary, grab the ArUCo parameters, and
        # attempt to detect the markers for the current dictionary
        arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)
        arucoParams = cv2.aruco.DetectorParameters_create()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)


        if len(corners) > 0:
            subprocess.Popen(["rosrun", "mavros", "mavsys", "mode", "-c", "LAND"])
            msg_str = "Marker ID: {}, Landed".format(ids)
            msg = String(msg_str)
            print(msg_str)
            pub.publish(msg)
            sub.unregister()
            # rospy.signal_shutdown("Landed")
        else:
            msg_str = "Marker ID: none, looking for marker"
            # print(msg_str)
            msg = String(msg_str)
            pub.publish(msg)

def main():
    rospy.init_node('aruco_listener')
    image_topic = "/camera/color/image_raw"
    global sub
    global pub
    sub = rospy.Subscriber(image_topic, Image, image_callback)
    pub = rospy.Publisher('/aruco/message', String, queue_size=10)
    rospy.spin()
    

if  __name__ == "__main__":
    main()
