#!/bin/sh

DESTINATION_DIR=`pwd`

cd coursesLangara/
./run.sh
if [ $? = "0" ]; then 
	cd ../
	cp coursesLangara/final.json roomLangara/
	cp coursesLangara/final.json filterAvailable/
	cd roomLangara
	python getDays.py

	if [ $? = "0" ]; then 
		echo "copying final.json, days.json"
		mv final.json $DESTINATION_DIR/all-courses-langara.json
		mv days.json $DESTINATION_DIR/all-days-data-langara.json
	else 
		echo " problem with scanning rooms" 
	fi 
	cd ../

	cd filterAvailable/
	python filter.py

	if [ $? = "0" ]; then 
		echo "copying avails.json"
		mv avails.json $DESTINATION_DIR/available-courses-langara.json
	else 
		echo "problem runing filter"
	fi
	cd ../

	cd newslangara/ 
	python scrape.py 
	mv news.json $DESTINATION_DIR/langara-news.json
	cd ../

	echo "done, waiting for new iteration"
	
else 
	echo "problem checking langara" 
	cd ../
fi
