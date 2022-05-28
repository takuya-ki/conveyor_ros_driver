cmake_minimum_required(VERSION 3.5)
project(conveyor)

find_package(catkin REQUIRED
  rospy
  std_srvs
  message_generation
)

add_service_files(
  FILES
  SetCommand.srv
)

generate_messages(
  DEPENDENCIES
)

catkin_package(
  CATKIN_DEPENDS rospy std_srvs message_runtime
)

catkin_install_python(
    PROGRAMS scripts/conveyor_driver.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
