#!/bin/bash

export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$(rospack find obstacle_avoidance)/models
gnome-terminal -- roslaunch obstacle_avoidance obstacle_avoidance.launch world_file:=$1 &&
cd ~/ardupilot/ArduCopter/ && sim_vehicle.py -v ArduCopter -f gazebo-iris --console



