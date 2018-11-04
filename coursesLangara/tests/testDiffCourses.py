#check to see what courses are different in the 2 files 
import json 

with open("../result.txt","r") as origin :
    with open("../final.json","r") as final :
        #parse the json
        ori = json.load(origin);
        fin = json.load(final);
        
        #counter
        diff = []
        for dep in fin : 
            for course in dep["courses"]:
                for offer in course["offerings"]:

                    has = False;

                    for course in ori : 
                        if course["subject"] == offer["subject"] and course["course"] == offer["course"] and course["section"] == offer["section"] :  
                            has = True;
                            break;
                    if has == False : 
                        print(course["subject"]," ",course["course"])

        

