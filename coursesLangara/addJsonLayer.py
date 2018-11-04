#import json for parsing
import json 

#open listDeps.json and results (the courses)
with open("templates/templateDeps.json","r") as lsDeps :
    with open("result.txt","r") as lsCrs : 
        #json parse for course infos:
        coursesData = json.load(lsCrs);

        #json template for departments (the highest layer)
        depsData = json.load(lsDeps);


        #iterate list of courses
        for course in coursesData : 
            #iterate list of departments
            for dep in depsData :

                #if a right department is found 
                if course["subject"] == dep["symbol"]:
                    hasGroup = False;
                    #iterate list of this dep's courses to find the right course group (same name + same Id, different section)
                    for ID in dep["courses"] : 
                        # if same name + same ID is found : 
                        if ID["course_id"] == (course["subject"]+" "+course["course"]):
                            #add this course to that group and stop current iteration 
                            ID["offerings"].append(course);
                            #confirm that this course has found its group
                            hasGroup = True;
                            break;
                    # else, if the course has not found its group:
                    if hasGroup == False:
                        # create a new group
                        newGroup = {}
                        newGroup["course_id"] = course["subject"]+" "+course["course"]
                        newGroup["offerings"] = [];
                        newGroup["offerings"].append(course);
                        
                        # add the new group to the depsData : 
                        dep["courses"].append(newGroup)
                    less = False
                    break

        #write to a file final.json
        with open("final.json","w") as writer : 
            writer.write(json.dumps(depsData,indent=4,sort_keys=True));
            print("done creating final.json")
