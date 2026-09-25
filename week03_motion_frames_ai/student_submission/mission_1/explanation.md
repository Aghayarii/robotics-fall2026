# Mission 1

## Error Source

A modeling or timing error happens when the robot does not move exactly as the motion model predicts, such as moving for a slightly different amount of time. A localization or measurement error happens when the robot moves correctly, but its position or orientation is measured incorrectly.

## Largest Error

The arc sequence had the largest discrepancy, with a position error of 0.538 m.

## Model Vs Observation

The observed motion matched the model pretty closely, but there were some small differences in the final position and angle. This could be caused by things like wheel slipping, simulation timing, or odometry error.

## Predictions

{'arc': {'x': 0.375, 'y': 0.386, 'theta': 1.6}, 'straight': {'x': 0.45, 'y': 0.0, 'theta': 0.0}, 'turn_then_drive': {'x': 0.0, 'y': 0.3, 'theta': 1.57}}

## Predictions Locked At

2026-09-25T20:37:21.150845+00:00

## Twice Distance

I would predict that the robot would travel twice as far, so it would move 0.90 m straight while keeping the same heading.
