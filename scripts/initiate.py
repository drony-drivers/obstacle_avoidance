#!/usr/bin/env python

from __future__ import print_function

import time
import sys
from set_mode import set_mode_client
from arm import arm_client
from takeoff import takeoff_client

if __name__ == "__main__":

    wait_time = 10
    print("Waiting for {} seconds before initiation".format(wait_time))
    time.sleep(wait_time)
    print("Initiation started!")
    while not set_mode_client(0, "GUIDED").mode_sent:
        print("Failed to set mode=GUIDED")
    while not arm_client(True).success:
        print("Failed to arm")
        time.sleep(1)
    while not takeoff_client(0, 0, 0, 0, int(sys.argv[1])).success:
        print("Failed to takeoff")
        time.sleep(1)

    print("Initiation done")