import json

with open("result.txt","r") as f :
    text = json.load(f);
    print(text,prettyprint=true);
