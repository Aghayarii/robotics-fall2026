# Mission 2

## Relationships

{'odom_to_base': 'odom → base_link', 'base_to_sensor': 'base_link → base_scan', 'map_role': 'Global frame corrected by localization or SLAM'}

## Point Answers

{'sensor_point_in_base': {'x': 0.97, 'y': 0.0}, 'sensor_point_in_odom': {'x': 0.54, 'y': 5.52}}

## Diagnostics

{'typo': 'Unknown frame name', 'wrong_source': 'Point interpreted in the wrong source frame', 'stale': 'Transform unavailable at the requested time'}

## Fixed Meaning

odom stays fixed to the odometry reference, base_link is fixed to the robot body, and base_scan is fixed to the sensor on the robot.

## Moving Coordinates

The robot's position and heading change relative to the odom frame. The sensor stays in the same position relative to base_link.

## Sensor Offset

The software needs to know where the sensor is mounted so it can correctly transform sensor measurements into the robot's frame or another frame.

## Map Absent

There may be no map frame because the lab is using odometry and is not running a mapping or localization system.
