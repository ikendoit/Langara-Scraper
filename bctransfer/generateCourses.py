from scrapePrint import grabDatas 
import json
import time

#open file
with open("texts/result.txt","r") as f : 
    #parse json
    text = json.load(f);

#keep time, assuming the server doesn't kick us out
timer = time.time();

#resume where we left off before getting dissed by their server
#resume = False;

#iterate courses + write to files
i = 0 ;
for course in text: 
    subj = str(course["Subj"]);
    ID = str(course["Crse"]);

    datas = str(grabDatas("LANG", subj,ID));

    f1 = open("eachCourse/"+subj+ID,"w+");
    f1.seek(0);
    f1.write(json.dumps(datas, sort_keys=True, indent=4));
    f1.close()
    time.sleep(2)
    i=i+1;
    print(str(subj)+ " -- "+str(ID))

print("this took: ", str(time.time() - timer));
print("waited in total: "+str(i)+" seconds");
