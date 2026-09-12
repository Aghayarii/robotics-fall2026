# Mission 2

## Predictions

{'straight': '0.45 meters from its starting point.', 'rotation': 'stay the same while its direction will turn to the left.', 'curve': 'right hand curved path because the robot is moving forward while the turning speed is negative, which makes it turn right.', 'curve_modified': 'This curve should be tighter and turn to the left because the turning speed is positive and relatively large compared with the forward speed.'}

## Prediction Locks

{'straight': '2026-09-12T01:30:53.949146+00:00', 'rotation': '2026-09-12T01:32:59.813698+00:00', 'curve': '2026-09-12T01:34:22.974465+00:00', 'curve_modified': '2026-09-12T01:35:56.651673+00:00'}

## Motion Comparison

My prediction was close to what happened. The robot moved about the amount I expected based on the measurements in the table.

## Measurement Explanation

The traveled path is the full distance the robot moved. The start-to-end distance is only the straight distance from the start to the finish.

## Safety Explanation

The command guard checks if the driving command is safe. The final zero command stops the robot when the movement is finished. The timeout is needed if commands suddenly stop, so the robot will stop automatically.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
