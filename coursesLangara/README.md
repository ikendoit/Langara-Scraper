******************************** COURSE _ LANGARA ********************************
@Author: Trung Kien Nguyen - Ken Nguyen

@github: github.com/ikendoit

@date: Oct 14th, 2017

@Version : 3.00

***********************************************************************************

Scrape for all courses of Langara-College at term 2019 - Spring (change link in python file to change terms)

turns datas to json, put in file "final.json"

this is for CourseHelper - a group project i am lending a hand to ! 

INSTRUCTION: 

    -   pip install json selenium lxml

    -   download phantomJS for the running OS, put executable file (should be in phantomjs/bin/) to the same folder as the python file 

	-   name that phantomJS executable "phantomjs"

    -   chmod 755 run.sh check.sh

    -   run : ./run.sh

    -   do : ./check.sh  to check for any departments lost

        +   if there is a lack of department, update name and code to template/templateDeps.txt

    -   read final.json for data loot

IN PROGRESS:

    - Completed, can do upgrade on algorithm but not immediate. 

POSSIBLE QUESTIONS:

    -   why not just make "final.json" straight away ? 
        
        +   i need to check for courses not recorded in "templateDeps", result.txt is a raw json file keeping raw datas of all possible course. If i make final.json right away, the template may not have the new department record.

    -   why not automate the department recording for the template ? 

        +   i am looking for an api for a site with full information. So far, "name" and "code" of all departments are not listed in a same page, or any convenient api. 

