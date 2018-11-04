#!/bin/sh

cd tests

if [ $(python testDiffCourses.py)]; then 
    echo "please update the courses shown above"
    echo "in template/templateDeps.txt"
else 
    echo "all courses are updated"
fi
