import requests;
import lxml.html


#get the subjectID from html in subID.txt, put into subIDs.txt file
f = open("subID.txt","r");
g = open("subIDs.txt","w+");
root = lxml.html.fromstring(f.read());
for element in root:
    print(element.attrib["data-code"] + " - "+ element.attrib["value"]);
    g.write(element.attrib["data-code"]+","+element.attrib["value"]+"\n");
f.close();
g.close();
