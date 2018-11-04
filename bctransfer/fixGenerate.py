from scrapePrint import grabDatas 
import json
import time

#open file
with open("texts/result.txt") as f : 
    #parse json
    text = json.load(f);

for course in text : 
    subj = str(course["Subj"]);
    ID = str(course["Crse"]);
    g = open("eachCourse/"+subj+ID,"r"); 
    if "no data found" in g.read(): 
        g1 = open("eachCourse/"+subj+ID,"w+"); 
        datas = str(grabDatas(subj,ID))
        print(datas);
        g1.write(datas);
        g1.close();
        print("worked on: ",subj,"  ",ID)
        time.sleep(2);
    g.close();
