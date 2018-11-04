#test to see if there is a new department coming up this term
import json

with open("../final.json","r") as final :

    f = open("../result.txt","r");

    res = json.load(f);

    f.close()

    #parse the json
    fin = json.load(final);
    
    deps = [];
    depsfin = []

    for dep in fin:
        for course in dep["courses"]:
            for offer in course["offerings"]:
                if offer["subject"] not in deps:
                    depsfin.append(offer["subject"])

    for course in res: 
        if course["subject"] not in deps :
            deps.append(course["subject"])

    for x in deps :
        if x not in depsfin : 
            print(x)
