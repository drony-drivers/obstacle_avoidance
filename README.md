# Obstacle Avoidance drone algorithm with Ardupilot and ROS

This is the ROS package we'll be working on.

## Dependencies
- mavros
- depthimage_to_laserscan
- slam_toolbox
- move_base
- explore_lite

## Installation

First follow all the instructions given in the `installation.md` file.

Then install mavros using the following instructions. (Taken from  [here](https://ardupilot.org/dev/docs/ros-install.html#installing-mavros))

``` sh
sudo apt-get install ros-melodic-mavros ros-melodic-mavros-extras
wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
chmod a+x install_geographiclib_datasets.sh
./install_geographiclib_datasets.sh
rm install_geographiclib_datasets.sh
```

Then, create a catkin workspace and clone this repository in the `src` folder. If you want to use ssh, change `git clone https://github.com/drony-drivers/obstacle_avoidance` command given below to `git clone git@github.com:drony-drivers/interiit21.git`.

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
Execute the following
``` sh
rosdep install obstacle_avoidance
```

## Running worlds

To run world 1, execute the following. (Same pattern for world 2 and 3)

``` sh
rosrun interiit21 start_sim_1.sh
```
