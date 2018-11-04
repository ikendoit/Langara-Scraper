import json

with open("./final.json","r") as f :
    data = json.loads(f.read());
    availCourses = [];

    for dep in data:  
        for course in dep["courses"]:
            curOffer = [];
            for offer in course["offerings"]:
                if offer["seats"] != "0" and offer["seats"] != "Cancel" and offer["seats"] != "":
                    curOffer.append(offer);
            course["offerings"]=curOffer;
            if (len(course["offerings"]) >0):
                availCourses.append(course);

    with open("./avails.json","w+") as g:
        g.write(json.dumps(availCourses, sort_keys=True, indent=4));
