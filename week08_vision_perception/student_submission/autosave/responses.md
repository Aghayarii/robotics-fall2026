# Lab 7 saved answers

## mission_1.diagnosis
My detector had trouble finding the mug because the wooden desk had similar colors. In `dim_1`, it selected a large area instead of just the mug. In `dim_absent`, it correctly found no contours because there was no mug.

## mission_1.limitations
The classical detector only uses colors and shapes, so it cannot actually recognize a mug. Changes in lighting, background, and object position can make it detect the wrong object or miss the mug completely. My box precision and recall were both only 15%.

## mission_2.comparison
I need the paired condition results table to give you accurate numbers. Scroll up to Section 2, Read the paired condition results, and send me a screenshot of that table.

## mission_2.choice
I recommend testing the learned detector further because it can recognize cups and predict their locations instead of relying only on color. I would start with a confidence threshold of 0.50 and compare its accuracy and processing time with the classical detector. For normal_1, the foreground mask had an IoU of 0.5756, but it also included unwanted pixels. This shows that a detailed mask does not necessarily identify the mug. One limitation is that our test uses a small collection of images, so the results may not represent real-world conditions.

## pillar_search.diagnosis
In my saved blue pillar attempt, the camera detected the blue pillar, and the mask showed its colored region. The robot used the centroid error to decide which direction to turn. As the error decreased toward zero, the pillar became centered. I kept the steering gain at 1.20, which worked well enough to complete the attempt. I did not change the setting, so I cannot compare improvements.

## pillar_search.evidence
My robot successfully completed all four colors: red, green, turquoise, and blue. None were missed. The state timeline showed the robot moving through the color sequence, and the camera evidence showed the blue pillar centered at the end. However, a centered colored region does not guarantee the correct object was detected because other objects can have similar colors. A stable hold also does not prove distance because the camera only provides image position, not depth.

## line_following.comparison
In the straight practice, the robot used the magenta mask to find the line and calculate how far it was from the center. The steering commands helped correct its direction. The curved track was more challenging because the robot needed to adjust its turning as the line changed direction. A larger image error required a stronger correction. I would compare the saved error graphs and commands to see whether the robot tracked smoothly or moved back and forth.

## line_following.limits
One possible failure is losing the magenta line when it moves outside the camera's view. This begins with missing visual information, so the controller stops instead of guessing where to go. For a real delivery robot, I would add depth cameras or lidar to detect obstacles and people. I would also test different lighting conditions, crowded areas, and emergency stopping before using the robot in a real environment.

## final.synthesis
In this lab, I learned how computer vision helps robots make decisions. In Mission 1, my classical detector had trouble locating the mug because the wooden desk had similar colors. Its box precision and recall were only 15%, showing that detecting colors does not always mean recognizing the correct object. I selected the learned detector for further testing.
In Mission 2, my robot completed the sequence of red, green, turquoise, and blue pillars in 21.8 seconds. The camera mask and centroid error helped the robot decide which direction to turn. However, detecting a colored region does not prove the object's identity or distance. In Mission 3, the robot used the magenta line to calculate steering corrections. The controller was designed to stop when it lost the line or received outdated camera information. This is important because a robot should not continue moving when it cannot reliably see its path.
Overall, I learned that successful detection does not guarantee safe robot behavior. A real robot would need additional sensors, obstacle detection, and more testing under different conditions.

## final.course_reflection
This lab helped me understand how computer vision is used in robotics. I enjoyed seeing how the robot could recognize colored pillars and follow a line using its camera. It was interesting to see how the robot's movements depended on what it detected.
One of the challenging parts was getting the detectors to recognize the correct objects. I learned that changes in lighting and background can affect how accurately a robot sees its surroundings. I also realized that even when a robot completes a task, it does not mean its decisions are always reliable.
This activity made me more interested in learning about robotics and AI because I got to see how the concepts we learn in class work in a simulation. It also showed me why safety is important, especially when robots are working around people. Overall, I enjoyed the hands-on experience and would like to work on similar projects in the future.
