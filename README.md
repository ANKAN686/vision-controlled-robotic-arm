# vision-controlled-robotic-arm
🤖 Hand-Tracked 3-DOF Robotic Arm

A real-time computer vision based robotic system where a 3-DOF servo robotic arm mimics the motion of a black ball held in a user's hand. The motion is detected using a webcam and processed using computer vision techniques, and the corresponding joint angles are sent to an Arduino-controlled robotic arm.

This project was developed as part of the Winter School Robotics Project. 

Problem statement (Winterschoo…

📌 Project Overview

The goal of this project is to design a vision-controlled robotic arm that follows the motion of an object detected by a webcam.

A laptop webcam continuously detects and tracks a black ball held in a participant’s hand. The system computes the object's motion and maps it to the joint angles of a 3-DOF robotic arm, allowing the arm’s end-effector to reproduce the motion.

The robotic arm movement is scaled by a configurable factor so that the arm can safely operate within its workspace. 

Problem statement (Winterschoo…

🎯 Objectives

The system is designed to achieve the following:

Detect and track a black object in real time using a webcam.

Convert the tracked motion into robotic arm joint commands.

Send commands from the laptop to an Arduino for servo control.

Demonstrate a working prototype where the arm follows the user's hand motion.

Provide documentation, source code, and a demonstration of the system. 

Problem statement (Winterschoo…

🧰 Hardware Requirements

The system requires the following hardware components:

3-DOF servo-based robotic arm

Arduino (Uno / Nano / Mega)

Laptop with webcam

Black ball or marker for tracking

Servo power supply (5–6V regulated)

USB cable

Basic wiring and mounting hardware

💻 Software Requirements

The software side of the project uses the following tools and libraries:

Python

OpenCV for computer vision

NumPy for numerical operations

Arduino IDE for servo control

Serial communication between laptop and Arduino

⚙️ System Architecture

The system operates through several modules working together:

Webcam Capture
The webcam captures real-time video frames of the scene.

Object Detection
The black ball is detected using color thresholding in HSV color space.

Object Tracking
The system continuously tracks the position and radius of the detected object across frames.

3D Position Estimation
The depth of the object is estimated using the known ball diameter and camera focal length.

Inverse Kinematics
The estimated 3D coordinates are converted into joint angles for the robotic arm.

Command Transmission
The computed joint angles are sent to the Arduino through serial communication.

Servo Control
The Arduino converts these commands into PWM signals that drive the servo motors.

🎥 Object Tracking Process

The object tracking process includes the following steps:

Capturing frames from the webcam.

Converting frames to HSV color space.

Applying color thresholding to isolate the black object.

Detecting the object's contour.

Calculating the centroid and radius of the detected ball.

Estimating the object's motion and position.

This process runs continuously to ensure smooth real-time tracking.

🧠 Motion Mapping

The detected motion of the ball is translated into robotic arm movement.

The mapping strategy includes:

Camera X coordinate → Base rotation

Camera Y coordinate → Shoulder movement

Motion direction → Wrist rotation

A scaling factor is applied to ensure that the arm moves safely within its physical limits. 

Problem statement (Winterschoo…

📊 Performance Requirements

The system aims to meet the following performance criteria:

Real-time tracking at at least 10 frames per second

Smooth robotic arm movement

Low latency between camera detection and arm motion

Stable tracking under normal indoor lighting conditions

🔧 Calibration

Before running the system, calibration is performed to:

Align the camera view with the robotic arm workspace

Detect the correct color range of the tracked object

Set scaling factors for motion mapping

Define safe limits for servo movement

🛡 Safety Features

To ensure safe operation, the system includes:

Servo angle limits

Reset functionality for tracking

Calibration mode for adjusting detection parameters

Manual stop control using keyboard input

These features help prevent unexpected or unsafe robotic arm movements. 

Problem statement (Winterschoo…

📂 Project Structure
hand-tracked-3dof-robotic-arm
│
├── vision
│   Ball tracking and object detection
│
├── kinematics
│   Inverse kinematics calculations
│
├── arduino
│   Servo motor control code
│
├── calibration
│   Color detection and system calibration
│
└── README.md
🚀 Future Improvements

Potential improvements for the project include:

Using deep learning based object detection

Adding depth sensing for more accurate 3D tracking

Implementing full 3D inverse kinematics

Creating a graphical user interface for calibration

Improving motion smoothing and stability

🛠 Technologies Used

Python

OpenCV

NumPy

Arduino

Serial Communication

Servo Motors

🎥 Demonstration

In the final demonstration, a participant moves a black ball in front of the webcam, and the robotic arm replicates the motion in real time.

If you want, I can also help you add two things that make robotics repositories look much more impressive on GitHub:

1️⃣ A system architecture diagram
2️⃣ A GIF demo section

These make the project look 10× more professional.

Sources
