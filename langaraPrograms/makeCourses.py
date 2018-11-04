#return a list (of lists) regarding courses of a program
#@param Program : name of program to fetch courses
#@param programs : dictionary to get information about Program
#@param url : based url 
#@param html : lxml.html object
#@param re : request object

#@return : generalList : list of all courses needed to complete

def getCourses(Program,programs,url,html,re):
    extension = programs[Program].replace("index.html","program-curriculum.html");
    r=re.get(url+extension);
    text=r.text;
    root = html.fromstring(text);

    datas = root.xpath("//div[contains(@class,'content-accordion')]");

    #prompt choice
    idc=0;
    for data in datas : 
        print(str(idc)+": "+data.xpath(".//a[contains(@class,'accordion-title')]")[0].text_content());
        idc=idc+1;
    choice = int(input("choose: "));

    #get courses
    generalList =[];
    if (choice >= 0 and choice <= idc):
        categories = datas[choice].xpath(".//tr[position() >1]");
        for course in categories : 
            courseList = [];
            minicourses = course.xpath(".//tr | .//div[@class='course-selection-title'] | .//div[contains(@class,'default_program-curriculum')]");
            for minicourse in minicourses : 
                element = minicourse.xpath(".//td[contains(@class,'course-number')]/a") 
                #filter duplicate display
                if element : 
                    if [element[0].text] not in generalList and element[0].text not in courseList: 
                        courseList.append(element[0].text)
                #show "one of" or "all of"
                elif minicourse.tag =="div" :
                    # beautify the string due to raw parsing and removing unicode character \xa0 
                    info =minicourse.text_content().replace(u"\xa0",u"").replace("\n"," ").replace("or"," or ");
                    courseList.append(info);
            #filter unneccessary list 
            if (len(courseList) >1) :
                generalList.append(courseList);

    return generalList;
