    *********************************************

 author: Trung Kien Nguyen -- Ken Nguyen

 date: Oct-19th,2017 

 scrapePrint : Program to get transferability of a course of a post-secondary school in BC - Canada

 version : 5.00

 functions: 

       1. Grab data from the bctransferguide.ca 

       2. Find and parse data of a course input by the user 

       3. print out possible transfers as list 

	   OR 

	   Scrape through all courses of langara, update database in eachCouse
		
			-	create eachCourse/ directory in same dir with python program

			-	python generateCourses.py ( warning: quite heavy )
    
 REQUIRE: 
    
    1. pip install requests
    
    2. pip install py27-lxml

    *****************************************

 INPUT FORMAT: python scrapePrint.py <school initial> <courseCode> <courseID> 

	eg : python scrapePrint.py LANG CPSC 1181 (enter)

    *****************************************

scrape transferabilities of a Langara course from bc transferguide.ca

 VERSION 5.00 : 
    
    -completed, full database in eachCourse/

    -whenever update is needed, run generateCourses.py to update json datas in eachCourse/ 

	-Finished TODO in 4.0 : 5.0 now scrape transferability for other institution
