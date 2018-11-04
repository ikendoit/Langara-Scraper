import json 
import sys

#format start,end to :00 or :30 format
def processHour(start,end):
    #set start time to kill in schedule
    if (start % 100) >= 0 and (start % 100) < 30 :
        start = ((start/100)) *100
    else :
        start = ((start/100)) *100 + 30
    #set end time to kill in schedule
    if (end % 100) >= 0 and (end % 100) < 30 :
        end = ( (end/100)) *100 + 30;
    else :
        end = ( (end/100)) *100 + 100 

    return start, end;
# direction : 
#    has a bunch of rooms: 
#        {} = day ; time 
#            day = monday,tuesday...
#            time = [8:30->9-20; ...]
            
#prepare hourList template
hours = open("dayTemplate.txt","r"); 
hourList = hours.read().split("\n")
hours.close()
hourList.remove("")
errors = 0;

#prepare dayList template
date = ["M","T","W","R","F","S"]

#create schedule template 
dataDay = {}
for unit in date :
    dataDay[unit] = hourList[:]

#prepare crn list
crns = [];
for arg in sys.argv: 
    crns.append(arg)

with open("final.json","r") as g : 
    allCourses = json.load(g);
    for course in allCourses : 
        for courseObj in course["courses"]:
            for offering in courseObj["offerings"]:
                #if found right crns
                if offering["course_num"] in crns : 
                    for section in offering["component"]: 
                        try : 
                            if "room" not in section or section['room'] == "WWW" or len(section["days"]) < 4 or len(section["time"]) < 4: 
                                #filter bad data
                                continue;
                            else : 
                                #check for used date, remove from schedule-free list, leaving only the free hours for the room 
                                #check through monday to saturday
                                start = int(section["time"].split("-")[0]);
                                end = int(section["time"].split("-")[1]);

                                #format start,end to :00 or :30 format
                                start,end = processHour(start,end);

                                #get monday to friday schedules of this room
                                for dateCode in dataDay.keys() : 
                                    #if found a matched date
                                    if section["days"].find(dateCode) > -1 :
                                        #scan the hours left in monday->friday schedule
                                        newHours = [];
                                        for hour in dataDay[dateCode]:
                                            if int(hour) < start or int(hour) >= end: 
                                                newHours.append(hour)
                                        dataDay[dateCode] = newHours
                                        print("vvvvvvvvvvvvvvv");
                                        print(newHours)
                        except (Exception) as e : 
                            #if time does not exist (on-site class)
                            errors+=1;
                            print("skipped an invalid "+courseObj["course_id"]+section["days"]+section["time"])
                            print(e)
                            continue;

    with open("timeCRN.json","w+") as writer : 
        print(str(errors)+" errors");
        writer.write(json.dumps(dataDay, indent=4,sort_keys=True));
