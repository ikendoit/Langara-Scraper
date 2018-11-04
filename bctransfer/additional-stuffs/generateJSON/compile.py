import json 
import glob

general =[] 
months = {
    "Jan/":"01"
    ,"Feb/":"02" 
    ,"Mar/":"03"
    ,"Apr/":"04"
    ,"May/":"05"
    ,"Jun/":"06"
    ,"Jul/":"07"
    ,"Aug/":"08"
    ,"Sep/":"09"
    ,"Oct/":"10"
    ,"Nov/":"11"
    ,"Dec/":"12"}

#generate general list (layer 0: MAIN JSON )
depsFile=open("../../templates/templateDeps.json","r")  

#the general JSON
general = json.load(depsFile);
depsFile.close()

for dep in general : 

#    try : 
    for courseName in glob.iglob("../../eachCourse/"+dep["symbol"]+"*"): 
        
        with open(courseName,"r") as course : 
            #filter for only courses that works
            school = course.read().split(", [");
            #layer 2 : courses id (number)
            data = {} 
            data["number"] = ""+courseName[-4:];
            data["institution"] = []
            
            #iterate through each school of transferability of each course
            for stringData in school: 
                #layer 3: institution
                institution= {}
                #beautify
                stringData = stringData.replace("[","").replace("]","");
                #get datas
                institution["school"]=stringData.split("', '")[0].replace("'","") 
                institution["properties"]= [] 
                #layer 4
                schoolProps = {}
                try : 
                    schoolProps["power"]=stringData.split("', '")[1].replace("'","");
                    #decode time
                    time = stringData.split("', '")[2].replace("'","");
                    print(time)
                    time = time.replace(time[:4],months[time[:4]]);
                    schoolProps["time"]=time
                except Exception as e :    
                    print "ERROR: generateing layer 4: ",e
                    continue

                #add layer 4 -> 3
                institution["properties"].append(schoolProps);

                #add layer 3 -> 2
                if len(institution) > 0 : 
                    data["institution"].append(institution);

            #add layer 2 -> 1 
            if len(data["institution"]) > 0 : 
                dep["courses"].append(data)
#    except e: 
#        print "problem reading files in eachCourse/: "+e

with open("./Langara.json","w+") as writer:
    writer.write(json.dumps(general,indent=4,sort_keys=True));
    print("done, check Langara.json")

