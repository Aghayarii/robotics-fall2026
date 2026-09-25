# Mission 3

## Specification

The robot should drive in a closed rounded rectangle using alternating straight segments and quarter-turn arcs. The motion commands should use linear and angular velocity to control the robot. The robot should stay within the required velocity limits and use the ROS coordinate convention. Each straight segment should move the robot forward, and each arc should turn the robot 90 degrees while continuing to move forward. After completing the full rounded rectangle, the robot should return close to its starting pose and send a final zero velocity command to stop. Tests should check the pattern structure, velocity limits, quarter-turn arcs, and final stop behavior.

## Original Prompt

Write Python code for a ROS 2 robot to drive a closed rounded rectangle using alternating straight segments and quarter-turn arcs. Use linear and angular velocity commands, keep the velocities within safe limits, and make sure the robot sends a zero velocity command at the end. Also include tests that check the motion pattern, velocity limits, geometry, and final stop behavior.

## Original Output

import math
import time

LINEAR_SPEED = 0.15
ANGULAR_SPEED = 0.5
STRAIGHT_TIME = 2.0
TURN_TIME = (math.pi / 2) / ANGULAR_SPEED


def rounded_rectangle_pattern():
    commands = []

    # Four sides with a rounded turn after each side
    for _ in range(4):
        commands.append({
            "linear_x": LINEAR_SPEED,
            "angular_z": 0.0,
            "duration": STRAIGHT_TIME
        })

        commands.append({
            "linear_x": LINEAR_SPEED,
            "angular_z": ANGULAR_SPEED,
            "duration": TURN_TIME
        })

    # Stop the robot at the end
    commands.append({
        "linear_x": 0.0,
        "angular_z": 0.0,
        "duration": 0.0
    })

    return commands


def test_pattern():
    commands = rounded_rectangle_pattern()

    # Check that the robot stops at the end
    assert commands[-1]["linear_x"] == 0.0
    assert commands[-1]["angular_z"] == 0.0

    # Check velocity limits
    for command in commands:
        assert abs(command["linear_x"]) <= 0.2
        assert abs(command["angular_z"]) <= 0.8

    # Check that there are four straight sections
    # and four rounded turns
    assert len(commands) == 9


if __name__ == "__main__":
    pattern = rounded_rectangle_pattern()

    for command in pattern:
        print(command)
        time.sleep(command["duration"])

## Ai Locked At

2026-09-25T21:35:07.333068+00:00

## Assumptions

The AI assumed that timing alone would make the robot follow the correct path and that the commanded velocities would match the robot's actual motion. It also assumed the robot starts from the expected pose and that the same timing will always produce a 90-degree turn.

## Problems

The code does not use ROS 2 to actually publish velocity commands to the robot. It also does not handle interruptions or guarantee that the robot stops if something goes wrong. The tests only check basic velocity limits and the final stop, so they do not fully test the segment order, turn geometry, heading, or interruption behavior.

## Modifications

I changed the AI-generated code so it correctly implements my assigned rounded rectangle pattern. I made it alternate between straight segments and quarter-turn arcs and kept the linear and angular velocities within the required limits. I also added and improved tests to check the number and order of segments, velocity limits, positive durations, and quarter-turn behavior.

## Test Argument

The tests check that the pattern is not empty, contains the correct 8 segments, and alternates between straight motion and turning. The velocity tests make sure the commands stay within the allowed limits. The duration test makes sure every segment has a valid positive duration. The quarter-turn test checks that each arc produces about a 90-degree turn. Together, these tests rule out an empty pattern, incorrect segment order, unsafe speeds, invalid durations, and incorrect turns.

## Remaining Limits

The unit tests show that the generated commands and pattern are correct, but they do not prove that the robot will behave perfectly in every real environment. Simulation and real robot behavior can be affected by timing, odometry error, wheel slip, or interruptions. The final stop and integration behavior also need to be verified during the ROS/Gazebo run.

## Ai Disclosure

I used ChatGPT to help review the AI-generated ROS code, understand errors, and develop and debug the tests. I did not assume the suggested code was correct. I reviewed the code, ran the unit tests and evaluation script, fixed errors, and checked the results myself. I am responsible for the final code, tests, and submitted work.
