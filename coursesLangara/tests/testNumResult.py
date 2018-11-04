#test if number of courses in final file same as number of courses in original result.txt file
import json 

with open("../result.txt","r") as origin :
    with open("../final.json","r") as final :
        #parse the json
        ori = json.load(origin);
        fin = json.load(final);
        
        #counter
        i=0;
        j=0;
        for dep in fin : 
            for course in dep["courses"]:
                for offer in course["offerings"]:
                    i = i+1; 

        for course in ori :
            j = j + 1; 

        print(i, " vs ",j);
        
        print("origin: ",origin.read().count("fees"))
        print("final: ",final.read().count("fees"))

