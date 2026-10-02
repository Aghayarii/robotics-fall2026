# mission_1 Submission

- Name: Alireza aghayari
- Section: CSCI 39536

## Explanations

### joint_gains

I adjusted the Kp, Ki, and Kd values for both joints until the arm could reach the targets and settle without too much oscillation. I increased Kp to make the joints respond more strongly, adjusted Kd to reduce overshoot, and changed Ki to help remove small remaining errors.

### gravity_comp

Gravity compensation helped the arm hold its position better, especially when the shoulder had to support the second link. Without it, the arm tended to sag more, but with it the joints stayed closer to the target and settled more smoothly.