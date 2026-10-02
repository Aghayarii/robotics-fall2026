# mission_3 Submission

- Name: Alireza Aghayari
- Section: CSCI 39536

## Explanations

### heading

The robot uses its estimated position to calculate the direction to the goal point. It compares that desired heading with its current heading to get an error. The PID controller then uses that error to create the steering command, with P reacting to the current error, I correcting persistent error, and D reducing overshoot.

### integration

A well-tuned controller can still fail because it depends on the robot’s estimated position. If the odometry is miscalibrated, the robot thinks it is somewhere different from its true position, so the PID may steer correctly based on the wrong information and still follow the wrong physical path.