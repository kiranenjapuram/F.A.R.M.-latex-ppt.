#! usr/bin/bash

gnome-terminal -e roscore       #we use gnome-terminal -e command for executing particular command on that terminal
rosrun agribot distance_pub.py   #publisher code
                                #new terminal open and executed each time we write gnome-terminal -e <command>





