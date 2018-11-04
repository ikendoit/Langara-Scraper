#boot up, categorize programs
def bootCategory(url,html,re):
   r = re.get(url+"index.html"); 
   text = r.text ; 
   root = html.fromstring(text) ;
   return root.xpath("//div[@class='category-column col-5 t-col-1 m-col-1']");

#boot up, show all programs
def bootAll(url,html,re):
   r = re.get(url+"index.html"); 
   text = r.text ; 
   root = html.fromstring(text) ;
   return root.xpath("//li[contains(@class,'t-col-3')]");
