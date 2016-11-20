# `trajectory_publishers`

A collection of ROS nodes that publish messages of the type `geometry_msgs/Point`.

## Usage

Make sure you have ROS installed on your computer.

```
roslaunch trajectory_publishers example.launch type:=<some_type>
```

Replace `<some_type>` with the trajectory that you want to publish, such as `circle` or `constant`.

## Add your own trajectories using `rospy`

1. Inherit from `abstract.Abstract`.
2. Redefine `compute_point` and, if needed, `__init__`.
3. Spawn an instance of your child class.
