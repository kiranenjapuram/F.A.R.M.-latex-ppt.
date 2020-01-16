#! /usr/bin/bash

#refer stepper_sub.py for why we did this there is some change in the code!
#this my1.bash is on rpi and my .bash is on
echo "angle is $1 anf flag is $2"  #this $1 is nothing but the data subscribe by rpi
declare -i flag=$2  #declaring flags
if (($flag == 1 ));  #if flag is 1
then
 ## <<--your servo motor code command for execution-->>  ## #execute sub file
fi
