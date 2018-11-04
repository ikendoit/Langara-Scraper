#@author: Trung Kien Nguyen -- Ken Nguyen
#@Student at   : Langara College 
#@Email : ikendoit1998@gmail.com
#@website : ikenweb-com.stackstaging.com
#@github: github.com/ikendoit
#personality : narcistic, arrogant, self-overestimate
#****************************************************

#Program scraper : 
#Scapes for courses neccessary for a program 
#to support Langara software developer club's group project 

#****************************************************


import lxml.html as html;
import requests as re;
from makeCourses import getCourses;
from makePrograms import makePrograms;
from makeBoot import bootCategory;
 
#***********************************
# variables
url = "https://langara.ca/programs-and-courses/";
datas = bootCategory(url,html,re);

#************************************
#choose category
i=0;
for data in datas : 
    print(str(i)+": "+data.xpath("div[@class='category-title']")[0].text_content());
    i=i+1;


#**********************************
#Show list of programs from a specific category
choice = int(input("I choose category: "));

if (choice >=0 and choice < 5) : 

    # get courses
    programs = makePrograms(datas,choice);

    # print courses + links for debug
    for program,key in programs.items() :
        print(program +" -- "+ key);
        print("\n");

#*****************************^********************
#show courses 

Program = str(raw_input("input exact program name (good format):  "));
if Program in programs :
    courseList = getCourses(Program,programs,url,html,re);
    for listy in courseList: 
        print(listy)

