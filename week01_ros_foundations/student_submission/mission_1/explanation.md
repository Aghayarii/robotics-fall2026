# Mission 1

## Command Path Explanation

A proposed command is transmitted via /student_cmd_vel. The guard checks whether the command is safe. Then the approved command is published on /cmd_vel so it can reach the robot.

## Graph Explanation

A ROS 2 graph shows how nodes communicate with each other through topics. For example, the course_cmd_vel_guard node communicates using the /cmd_vel topic.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found the ranges field, which represents LiDAR distance measurements around the robot in meters.

## Tools Explanation

Gazebo is responsible for simulating the robot and its environment, while RViz is responsible for displaying ROS 2 information so the user can visualize what the robot is sensing and doing.
