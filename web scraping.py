import requests
from bs4 import BeautifulSoup
import re
r=requests.get("https://maktabkhooneh.org/plus/")
soup=BeautifulSoup(r.content,"html.parser")
res=soup.find_all("div",attrs={"class":"course-card__title"})
res1=soup.find_all("div",attrs={"class":"course-card__uni-title"})
subtitute= [re.sub(r"\s+","",item1.text).strip() for item1 in res1]
course=[re.sub(r"\s+","",item.text).strip() for item in res]

course_tag=list()
for item1 in subtitute:
    item1=''.join(item1.split('\u200c'))
    course_tag.append(item1)
for i in range(len(course)):
    if course_tag[i]=='مکتبخونه':
        print(course[i])


        



