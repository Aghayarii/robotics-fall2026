# mission_2 Submission

- Name: Alireza Aghayari
- Section: CSCI 39536

## Explanations

### calibration

I adjusted the wheel radius and track width while comparing the odometry estimate to the true robot path. I kept changing the values until the estimated distance and turns matched the actual motion more closely and the error became small.

### drift

Odometry can still drift because small measurement errors build up over time. Wheel slip, encoder noise, timing errors, and small differences in wheel size or track width can all make the estimated position slowly move away from the robot’s true position.