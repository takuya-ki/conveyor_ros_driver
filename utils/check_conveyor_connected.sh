#!/bin/bash

byobu new-session -d -s bringup
byobu select-pane -t 0
byobu split-window -v
byobu select-pane -t 0
byobu split-window -h
byobu select-pane -t 2
byobu split-window -h

byobu send-keys -t 0 'roscore' 'C-m'
sleep 2.
byobu send-keys -t 1 'rosrun conveyor conveyor_driver.py _/conveyor/ip:=169.0.0.1' 'C-m'
sleep 2.
byobu send-keys -t 2 'rosservice call /conveyor/set_command nl' 'C-m'
sleep 3.
byobu send-keys -t 3 'rosservice call /conveyor/set_command complete' 'C-m'

byobu attach -t bringup
