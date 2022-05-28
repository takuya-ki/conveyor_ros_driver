# conveyor_ros_driver

ROS driver for conveyor belt.

## Start this driver
    $ rosrun conveyor conveyor_driver.py  

## Send a predefined command  
    $ rosservice call /conveyor/set_command "<refer to below>"  

## Available commands  
- nl: normal rotation with low speed  
- nm: normal rotation with middle speed  
- nh: normal rotation with high speed  
- rl: reverse rotation with low speed  
- rm: reverse rotation with middle speed  
- rh: reverse rotation with high speed  
- stop: stop the motion  
- complete: finish program  
