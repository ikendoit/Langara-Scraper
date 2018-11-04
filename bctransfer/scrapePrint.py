import requests
import lxml.html
import sys
import json

# author: Trung Kien Nguyen -- Ken Nguyen
# ikenweb-com.stackstaging.com
# date: Sep-15th,2017 
# scrapePrint : Program to get transferability of a course of a secondary institution
# functions: 
#       1. Grab data from the bctransferguide.ca 
#       2. Find and parse data of a course input by the user 
#       3. print out possible transfers as list 
# input format: python scrapPrint.py <school initial> <courseCode> <courseID> (input in string type with "" )


#*****************************************************************
# grab info from print site, return json 
#   name : string 
#   data : [] 
#       Date : string 
#       To : string 
#       Credit : string
def grabDatas(school,course, ID):
    #*****************************************************************
    #grab the subject ID from subID.txt, return "wrong code" if cant find course
    subID =""
    for line in open("texts/"+school+".txt","r"):
        if len(line) < 7 : 
            schoolID = line.replace(" ","").replace("\n","");
        if course == line.split(" - ")[0]: 
            subID = line.split(" - ")[1];
    if subID== "":
        return "wrong course" ; 

    #*****************************************************************
    #requests datas
    r= requests.get("http://www.bctransferguide.ca/TGSearch/Search/PrintResult?SearchTerm="+school+"+"+course+"+"+ID+"&CurrentPageNumber=1&ResultsPerPage=9999999&InstitutionId="+schoolID+"&SubjectId="+subID+"&CourseNumber="+ID+"&TransferDirection=Sending&YearCourseCompleted=0");

    #*****************************************************************
    # some variables, return "no data found if cant find any data"
    text = r.text;

    root = lxml.html.fromstring(text);

    datas = root.xpath("//*[@class='row rowWrapper']");

    if (not datas):
        return "no data found";

    courses = {}
    courses["Name"] = school+course+ID
    courses["Data"] = []

    #dictionary for school names
    try : 
        f = open("texts/schools.txt","r");
        schoolDict = eval(f.read())
        f.close();
    except : 
        print("schools.txt not found");


    #*****************************************************************
    #parse datas
    #get the datapacks, return a list
    try :
        for data in datas: 
            #list of transfers
            read = data.xpath("//div[@class='row']");
            for element in read:
                #a single transfer
                minicourse = {};
                #check to/ credit / date
                i = 0;
                for subelement in element:
                    context = subelement.text_content()
                    if (context==""):
                        continue
                    context = context.strip().replace("\n","").replace("\r","");

                    if context in schoolDict.keys(): 
                        context = context +" - "+ schoolDict[context];
                       
                    if i == 0 : 
                        minicourse["To"] = context;
                    elif i == 1 : 
                        minicourse["Credit"] = context;
                    elif i == 2 : 
                        minicourse["Date"] = context;
                    i = i+1;

                #get newest, still effective transfer
                if len(minicourse) > 2 and "-" in minicourse["Date"]:
                    courses["Data"].append(minicourse);


    except (Exception) as e :
        print("problem scraping data: "+str(e));

    return courses;


#*****************************************************************
# run the program, print each transfer opportunity as a list
# params :  
#   1 : school code : LANG UBC ...
#   2 : Course code : BIOL MATH ...
#   3 : course id : 1171 1280 .....
if len(sys.argv) ==4 :
    school = sys.argv[1]
    course = sys.argv[2];
    ID = sys.argv[3];
    course = grabDatas(school,course,ID);
    print(json.dumps(course,sort_keys=True, indent=4));
    print("\n\n");
