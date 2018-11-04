#!/bin/bash

START=$SECONDS 

python getCourses.py
python addJsonLayer.py
echo "done, all are in final.json"

durati=`expr $SECONDS - $START`
echo "$durati seconds"
