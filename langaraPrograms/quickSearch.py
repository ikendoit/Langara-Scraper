import sys
import lxml.html as html;
import requests as re;

from makeCourses import getCourses;
from makePrograms import makeProgramsQuick;
from makeBoot import bootAll;

if len(sys.argv) == 2 :
    url = "https://langara.ca/programs-and-courses/";
    datas = bootAll(url,html,re);

    for data in datas : 
        if (data.text_content() == sys.argv[1]):
            print("found");
            programs = makeProgramsQuick(data);
            lists = getCourses(sys.argv[1],programs,url,html,re);
            for list in lists : 
                print(list);
                print("\n");

            break; 

