#!/bin/sh

# automate: generate a list of available classrooms in Langara

#filter all rooms 
cat final.json | grep "room" | uniq > rooms.txt
sed -i -e "s/.*\"room\"\: \"//g" -e "s/\"\,//g" -e "/^ $/d" -e "/WWW/d" -e "s/ //g"  rooms.txt

#create room list in rooms.txt
cat rooms.txt | sort | uniq > $$ && cat $$ > rooms.txt  && rm $$
