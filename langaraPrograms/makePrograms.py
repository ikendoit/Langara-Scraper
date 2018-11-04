#generate a dictionary of available programs and links to them
#@param : datas : datas containing html
#@param : choice : index of category
#@return : programs : dictionary for program name + link to program

def makePrograms(datas,choice):
    categories = datas[choice].xpath(".//li[contains(@class,'t-col-3')]") 
    programs = {}
    for data in categories: 
        context = data.text_content();
        # check invalid information
        if (context=="" or context=="\n" or context=="\r" or context=="No Results"):
            continue;
        # strip them off, keep the change
        context=context.strip().replace("\n","").replace("\r","").replace("  ","").replace("\t","");
        programs[context] = data.xpath("a")[0].get("href");

    # return a dictionary of names and values
    return programs;

# makeProgram for quick search 
# generate dict of a program and its link
# @param : data  html 
# @return : programs : dictionary for program name + link to program
def makeProgramsQuick(data):
    programs = {}
    for content in data: 
        context = content.text_content();
        # check invalid information
        if (context=="" or context=="\n" or context=="\r" or context=="No Results"):
            continue;
        # strip them off, keep the change
        context=context.strip().replace("\n","").replace("\r","").replace("  ","").replace("\t","");
        programs[context] = data.xpath("a")[0].get("href");

    # return a dictionary of names and values
    return programs;
