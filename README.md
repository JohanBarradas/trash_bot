# Trash Collecting Robot MK.I

Code for a trash collecting robot, includes autonomous navigation.

## The essential hardware components for this project are as follows:

- 1 Nvidia Jetson Nano
- 1 Roboteq SDC2130 motor controller
- 1 Neato LIDAR Laser Distance Sensor LDS xv Series xv-11
- 2 12V DC motors with encoders
- 1 12V DC motor (for brush/collecting)
- 2 DC servo motors
- 1 L298N Stepper Motor Driver Controller Board Dual H Bridge Module
- 1 Songle 5V Single Relay Module (D25)

###### This code was made in collaboration with Shreyosi Endow and Chris Collander

## To run:

1) Have the **Robot Operating System(ROS)** properly installed and setup 
2) clone this repository to your catkin workspace
3) **catkin_make**
4) run the "initialize" bash script to initalize all the required variables for the robot
5) on a new terminal run roslaunch trash ugv.launch
6) on a new terminal run roslaunch trash move_base.launch
7) Provide goals to the robot by using Rviz from a remote machine 

## To turn on the Collecting mechanism: 
1) Make sure the relay is properly connected to the Jetson Nano (on GPIO)
2) run brush.py located in the python&helpfulscripts folder

## To turn on the Dispensing mechanism:
1) Make sure the motor driver is properly connected to the Jetson Nano (on GPIO)
2) run yeet.py located in the python&helpfulscripts folder

###### NOTE: stay clear from the back of the bot when dispensing
