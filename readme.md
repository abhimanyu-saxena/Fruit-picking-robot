ENPM-662: INTRODUCTION TO ROBOT MODELLING
PROJECT 2
-----------------------------------------------------------------------------------------------------------------------

Instructions to run the project:

Step 1: Get required folders
-> copy the folders "basket_assmebly", "husky" and "manipulator_v5" in the {name of your catkin workspace}/src folder

Step 2: Build catkin
-> open terminal window and run commands
-> cd {name of your catkin workspace}
-> catkin_make
-> source devel/setup.bash

Step 3: Spawn robot in Gazebo
-> open terminal and run the commands
-> roslaunch husky template_launch.launch

Step 4: Run teleop code (chmod +x .py files if required)
-> open new terminal window and run commands
-> cd src/husky/src
-> python3 teleop_template.py
-> use commands to reach a tree in the world

Step 5: Command the manipulator
-> open new terminal window
-> cd src/husky/src
-> python3 joint_pub.py
Note: The robot spawns with default configuration of all joint angles as 0 degrees
-> Enter 1 for home configuration: to see the world
   Enter 2 for pick cofiguration: Pose for picking the fruit
   Enter 3 for place cofiguration: Pose to place picked fruit in basket
   Enter 0 to exit

Step 5: To see camera output in rviz/rqt_image_view
-> open new terminal window
-> rviz
-> add camera and subscribe to /image_raw topic
-> (alternatively) run rqt_image_view and subscribe to /image_raw topic
