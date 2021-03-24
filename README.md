# Obstacle Avoidance drone algorithm with Ardupilot and ROS

This is the ROS package we'll be working on.

## Dependencies
- mavros
- depthimage_to_laserscan
- slam_toolbox
- move_base
- explore_lite

## Installation

First follow all the instructions given in the `installation.md` file. (The same instruction file given at the beginning)

Then install mavros using the following instructions. (Taken from [here](https://ardupilot.org/dev/docs/ros-install.html#installing-mavros))

``` sh
sudo apt-get install ros-melodic-mavros ros-melodic-mavros-extras
wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
chmod a+x install_geographiclib_datasets.sh
./install_geographiclib_datasets.sh
rm install_geographiclib_datasets.sh
```

Then, create a catkin workspace and clone this repository in the `src` folder. 

``` sh
cd ~
mkdir -p ardupilot_ws/src
cd ardupilot_ws/src
git clone https://github.com/drony-drivers/obstacle_avoidance
chmod +x interiit21/start_sim*.sh
cd ..
catkin_make
```

Finally, execute the following commands to add necessary lines to your `~/.bashrc`

``` sh
echo 'source ~/ardupilot_ws/devel/setup.bash' >> ~/.bashrc
```

### Install ROS dependencies

``` sh
  sudo apt install ros-melodic-depthimage-to_laserscan ros-melodic-explore-lite ros-melodic-geometry-msgs ros-melodic-mavros ros-melodic-mavros-msgs ros-melodic-move-base ros-melodic-roscpp ros-melodic-rospy ros-melodic-sensor-msgs ros-melodic-slam-toolbox ros-melodic-std-msgs 

  rosdep install obstacle_avoidance
```
### Additional dependencies

``` sh
pip install imutils
```

## Running worlds

To run a Gazebo world, `rosrun obstacle_avoidance <world_file>`  execute the following. If `<world_file>` is "interiit_world1.world", then run the following. Note that all the world files must be present in the `worlds` folder.

``` sh
rosrun obstacle_avoidance start_sim.sh interiit_world1.world
```
