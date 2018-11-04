import requests as re 
import lxml.html
import lxml.etree
import json

caller = re.get("https://langara.ca"); 
text = caller.text; 
root = lxml.html.fromstring(text)

newsets = root.xpath('//*[@id="wrapper"]/div[3]/main/div[4]/div/div');

data = []

for news in newsets[0] : 
    data.append({
        "text": news.xpath(".//p")[0].text_content(),
        "img": news.xpath(".//img")[0].attrib["src"],
        "link":news.xpath(".//a")[0].attrib["href"],
    })

with open("news.json","w+") as f :  
    f.write(json.dumps(data,indent=4, sort_keys=True));

