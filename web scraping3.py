import mysql.connector
from sklearn import tree
cnx = mysql.connector.connect(user="root", password="mypass",host="127.0.0.1",database="product")
cursor = cnx.cursor()
import requests
from bs4 import BeautifulSoup
import re
kala=input("")
cursor.execute("delete from product")
x=[]
y=[]
for i in range(1,6):

    #page=requests.get("https://www.digikala.com/search/?q=%s&sortby=22" %(kala))
    page=requests.get("https://www.digikala.com/search/?has_selling_stock=1&q=%s&pageno=%i&sortby=22" %(kala,i))
    soup=BeautifulSoup(page.content,"html.parser")
    data=soup.find(class_="c-listing__items")
    product=data.find_all(class_="c-product-box__title")
    price=data.find_all(class_="c-price__value-wrapper")
    product1=[re.sub(r"\s+","",item.text).strip() for item in product]
    price1=[re.sub(r"\s+","",item1.text).strip() for item1 in price]
    #print(price1)
    #print(product1)
    
    for i in range(0,36): 
        cursor.execute("INSERT INTO product VALUES (\"%i\",\"%s\",\"%s\")" %(i,product1[i],price1[i]))
        #query = ("SELECT * FROM product")
cursor.execute("SELECT * FROM product")
x=[]
y=[]
for (contact_id,product1,price1) in cursor:
    #print("%i, %s, %s"%(contact_id, product1, price1))
    #product1=re.search(r"مدل(.*)\d",product1)
    product1=''.join(product1.split('\u200c'))
    x.append(product1[10:])
    y.append(price1)

#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(x,y)
#new_data = [[190,89,43],[160,56,39]]
#answer = clf.predict(new_data)
#print(answer[0])
#print(answer[1])
#print(x)
#print(y)

cnx.commit()

