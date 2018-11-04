import json

with open("../final.json","r") as final :

    #parse the json
    fin = json.load(final);
    
    for dep in fin:
        for course in dep["courses"]:
            if (len(course["offerings"])) > 1 : 
                print(course["course_id"])
#            for offer in course["offerings"]:
#                if offer["subject"] not in deps:
#                    depsfin.append(offer["subject"])
#
