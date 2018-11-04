import platform
from selenium import webdriver
import lxml.html
import json

# use headless web driver due to cookie requirement
#*********************************************************************

if platform.system() == "Windows": 
    PHANTOMJS_PATH = "./phantomjs.exe"
else : 
    PHANTOMJS_PATH = "./phantomjs"

browser = webdriver.PhantomJS(PHANTOMJS_PATH)

browser.get("http://swing.langara.bc.ca/pls/prod/hzgkfcls.P_Sel_Crse_Search?term=201910");

browser.find_element_by_xpath("//*[@id='GetCrseForm']/table/tbody/tr[3]/td/p[2]/input[1]").click()

#scrape main page
#*********************************************************************
root = lxml.html.fromstring(browser.page_source);

#get courses
myList = root.xpath("//form/table/tbody/tr[.//td[@class='dedead']]");

#dict for json keys
#there are 19 properties, from inside out : 
#   -   first layer has 4
#   -   second layer has 16 (1 is a list of the 1st layer)
departmenLayer = {};
courseLayer = {1:"rp",2:"seats",3:"waitlist",4:"sel",5:"course_num",6:"subject",7:"course",8:"section",9:"credits",10:"title",11:"fees",12:"repeat_limit",13:"component",19:"instructor",16:"non_standard_start",17:"non_standard_end"}
componentLayer ={13:"type",14:"days",15:"time",18:"room"}

#generate Jsonlist
genList = [];

f = open("result.txt","w+");

#iterate through courses
for element in myList: 
    #properties of a course
    myList1 = element.xpath(".//td")
    i=1
    miniList = {}
    #create a list of components to store different rows
    miniList["component"] = [];
    #iterate through properties
    for element1 in myList1: 
        textFound = element1.text_content().replace(u"\xa0",u"").replace(u"\u2014",u"").replace("\n","")
        if (i >= 13 and i <=15) or (i == 18) :
            if i == 13 :
                miniList["component"].append({})
            miniList["component"][-1][componentLayer[i]] = textFound;
        else :        
            if len(miniList) <16:
                miniList[courseLayer[i]]=textFound
            if i == 6 and textFound == "": 
                miniList = genList[-1]; 
                genList.pop();
        i=i+1
    if len(miniList) >10 and miniList["subject"] != "": 
        genList.append(miniList)
f.write(json.dumps(genList,indent=4,sort_keys=True));
f.close();
print("done")
