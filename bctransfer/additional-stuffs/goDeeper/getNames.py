#get school names, put in a txt file : schools.txt
#get courses of schools (subID and data-code), put in the right text file in directory: Deeper

from selenium import webdriver
import requests;
import lxml.html;
import time

try : 
    browser = webdriver.PhantomJS("./phantomjs");

    browser.get("http://www.bctransferguide.ca/search/course");

    schools = browser.find_element_by_xpath("//select[@id='Institutions']").find_elements_by_tag_name("option")

    for i in range(0,len(schools)):
        school = schools[i];
        if school.get_attribute("data-code") :
            print(school.get_attribute("data-code") );
            school.click();
            time.sleep(1); 
            subjs = browser.find_element_by_xpath("//select[@id='Subjects']").find_elements_by_tag_name("option")
            subjWriter = open("./Deeper/"+school.get_attribute("data-code")+".txt","w+");
            subjWriter.write(school.get_attribute("value")+"\n");
            for subj in subjs : 
                if subj.get_attribute("data-code") :
                   subjWriter.write(subj.get_attribute("data-code")+" - "+ subj.get_attribute("value") + "\n");

            subjWriter.close();
            schools = browser.find_element_by_xpath("//select[@id='Institutions']").find_elements_by_tag_name("option")
except : 
    print("problem with internet connection");
