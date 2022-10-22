# conveyor_ros_driver

ROS driver for conveyor belt.

## Dependency


## Installation

    $ cd catkin_ws/src
    $ git clone https://github.com/takuya-ki/conveyor_ros_driver.git --depth 1
    $ cd ..; catkin build

## Usage

### Start this driver
    $ roscore  
    $ rosrun conveyor conveyor_driver.py _/conveyor/ip:=169.0.0.1  

### Send a predefined command  
    $ rosservice call /conveyor/set_command "<refer to below>"  

### Available commands  
- nl: normal rotation with low speed  
- nm: normal rotation with middle speed  
- nh: normal rotation with high speed  
- rl: reverse rotation with low speed  
- rm: reverse rotation with middle speed  
- rh: reverse rotation with high speed  
- stop: stop the motion  
- complete: finish program  

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
