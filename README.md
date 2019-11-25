# Langara Scraper Suite 

A part of this suite was used in a cron job for this app [EduRidge](https://www.youtube.com/watch?v=MWfDuXaSP6M)

First, a cli introduction: https://www.youtube.com/watch?v=auEVoUIkh6s&feature=youtu.be

## Functions: 

* Extract 
	* Data for all courses
	* Front page of Langara News
	* BCTransfer Page to see transferability of any course in Langara. ( eg: what courses of all BC's universities can Langara's CPSC1181 transfer to ? )
	* Available courses with open seats.
	* Classroom data and when they are free so we can have a nap in.
	* Langara Program data, so that we know what courses to take to finish a Langara Program.
	* Data of free time a student has based on their courses ID (which are given as CRN codes)
	* And more! It has been so long I think I went crazy and pumped hidden features back then.


## How To Run

* Download [phantomJS](https://phantomjs.org/download.html) headless
* Add phantomJS .exe file in `"./coursesLangara/"` directory with name `"phantomjs"`
* Grant permission to update.sh by entering in command line: [chmod 775](https://chmodcommand.com/chmod-775/) update.sh
* ./update.sh
* Check this directory for Langara files (destination directory can be modified in update.sh)


## Credits: 

  - Langara Software Developer club, who inspired me to make this suite to support their phone application ( mentioned above ) as well as internal tools
