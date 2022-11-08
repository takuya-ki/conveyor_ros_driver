# conveyor_ros_driver

[![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.svg)](http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

ROS driver for conveyor belt.

## Dependency

- ROS Kinetic/Melodic/Noetic
- [takuya-ki/conveyor_modbus](https://github.com/takuya-ki/conveyor_modbus)

## Installation

```bash
$ cd catkin_ws/src  
$ git clone https://github.com/takuya-ki/conveyor_ros_driver.git --depth 1  
$ cd ..; catkin build  
```

## Usage

### Operations with two computers  
1. Execute a control server on an Windows computer (refer to [conveyor_modbus](https://github.com/takuya-ki/conveyor_modbus))  
 
```bash
$ python src/commands.py --command_from external --ip 169.0.0.1
```

2. Start a command server on an Ubuntu computer

```bash
$ roscore  
$ rosrun conveyor conveyor_driver.py _/conveyor/ip:=169.0.0.1  
$ rosservice call /conveyor/set_command "<refer to below>"  
```

##### Available commands  
- nl: normal rotation with low speed  
- nm: normal rotation with middle speed  
- nh: normal rotation with high speed  
- rl: reverse rotation with low speed  
- rm: reverse rotation with middle speed  
- rh: reverse rotation with high speed  
- nXX (rYY): drive with a set of rotation and speed [Hz/100] values  
- stop: stop the motion  
- complete: finish program  

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
