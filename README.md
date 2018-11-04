# Langara Scraper Suite 

A part of this suite was used in a cron job for this app - EduRidge: https://www.youtube.com/watch?v=MWfDuXaSP6M

First, a cli introduction: https://www.youtube.com/watch?v=auEVoUIkh6s&feature=youtu.be

## Functions: 

```
  - Scrape Langara all courses Data.
	- Scrape Langara News on the front page. 
	- Scrape BCtransfer page to see transferability of any course in Langara. ( eg: what courses of all BC's universities can Langara's CPSC1181 transfer to ? )
	- Extract data of available courses left to register.
	- Extract data of classrooms in Langara and when they are free so we can have a nap in.
	- Extract data of Langara's Programs, so that we know what courses to take to finish a Langara Program.
	- Extract data of free time a student has based on their courses ID ( which are given as CRN codes )
	- And more, It has been so long I think I went crazy and pumped hidden features back then.
```

## How To Run:
```
	- download phantomJS headless, add in "./coursesLangara/" directory as file "phantomjs"
	- chmod 775 update.sh
	- ./udpate.sh
	- check this directory for Langara files (destination directory can be modified in update.sh)
```

## Credits: 

  - Langara Software Developer club, who inspired me to make this suite to support their phone application ( mentioned above ) as well as internal tools
