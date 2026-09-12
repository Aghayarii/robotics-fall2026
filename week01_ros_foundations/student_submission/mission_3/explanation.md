# Mission 3

## Data To Command

The first function looks at the LiDAR readings in front of the robot and finds the closest valid distance. The second function uses that distance to decide whether the robot should move forward or stop.

## Missing Data Safety

It stops because missing sensor data could be unsafe. If the robot cannot tell whether something is in front of it, stopping is the safer choice.

## System Layers

The decision functions decide if the robot should move or stop. The ROS node gets the LiDAR data and uses those functions. The command guard checks the movement command before it is sent to the robot.
