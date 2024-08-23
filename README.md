# AWS EC2 Instance Management using Hand Gestures

This code demonstrates how to manage AWS EC2 instances using hand gestures captured by a webcam. It uses the OpenCV library for capturing webcam video and the HandTrackingModule from the cvzone library to detect hand gestures. The code allows launching and terminating EC2 instances based on detected gestures.

# How the Code Works

The code does the following:
1. Captures webcam video using OpenCV.
2. Detects hand gestures using the HandTrackingModule.
3. Recognizes hand gestures to trigger AWS EC2 instance actions.
   Index finger up: Launch an EC2 instance.
   Thumb up: Terminate the most recently launched EC2 instance.
4. Manages AWS EC2 instances based on detected gestures.

# Usage
1. Make sure you have OpenCV and cvzone installed: pip install opencv-python-headless cvzone boto3.
2. Configure your AWS credentials using aws configure or by setting environment variables.
3. Replace the values in the ImageId and SecurityGroupIds parameters in the myOSLaunch function with your own values.
4. Run the script using a Python interpreter.
5. The script will open a webcam feed. Use hand gestures to launch and terminate AWS EC2 instances.

# Notes

1. The code assumes that you have an active AWS account and appropriate permissions to manage EC2 instances.
2. This code provides a basic example of using hand gestures to control AWS resources.

# Important
Please exercise caution when using AWS resources and be aware of potential costs associated with running EC2 instances.




