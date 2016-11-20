# `trajectory_publishers`

A collection of ROS nodes that publish messages of the type `geometry_msgs/Point`.

## Installation

Type this in a terminal.
This should work if you have ROS and `catkin_tools` installed on your computer.

```
cd <your_catkin_workspace>/src
git clone https://github.com/adaldo/trajectory_publishers
cd <your_catkin_workspace>
catkin build
source devel/setup.bash
```

## Usage

Type this in a terminal.

```
roslaunch trajectory_publishers example.launch type:=<some_type>
```

Replace `<some_type>` with the trajectory that you want to publish, such as `circle` or `constant`.

## Adding your own trajectories using `rospy`

1. Inherit from `abstract.Abstract`.
2. Redefine `compute_point` and, if needed, `__init__`.
3. Spawn an instance of your child class.
