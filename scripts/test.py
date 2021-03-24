#!/usr/bin/env python



# rospy for the subscriber
import rospy
# ROS Image message
from sensor_msgs.msg import Image
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import cv2
import imutils

bridge = CvBridge()

def image_callback(msg):
    print("Recieved an image!")
    try:
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as e:
        print(e)
    else:
        time = msg.header.stamp
        cv2.imwrite('./img_taken/'+str(time)+'.jpeg', cv2_img)
        ARUCO_DICT = {

        "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000

        }

        image = cv2_img
        image = imutils.resize(image, width=600)
        # loop over the types of ArUco dictionaries
        arucoName = "DICT_5X5_1000"
        arucoDict = cv2.aruco.DICT_5X5_1000
        # load the ArUCo dictionary, grab the ArUCo parameters, and
        # attempt to detect the markers for the current dictionary
        arucoDict = cv2.aruco.Dictionary_get(arucoDict)
        arucoParams = cv2.aruco.DetectorParameters_create()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)



        # if at least one ArUco marker was detected display the ArUco
        # name to our terminal
        if len(corners) > 0:
            print("[INFO] detected {} markers for '{}'".format(len(corners), arucoName))
        else:
            print("[INFO] not detected")
        rospy.sleep(1)

def main():
    rospy.init_node('image_listener')
    image_topic = "/camera/color/image_raw"
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.spin()

if  __name__ == "__main__":
    main()