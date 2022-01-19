import mysql.connector
cnx = mysql.connector.connect(user="root", password="mypass",host="127.0.0.1",database="email")
cursor = cnx.cursor()
import re
username=input("")
password=input("")
re.search(r".+\@\w+\.\w+$",username)

while re.search(r".+\@\w+\.\w+$",username)==None:
    print("expression@string.string")
    username=input("")
    password=input("")
    
cursor.execute("INSERT INTO email VALUES (\"%s\",\"%s\")"%(username,password))
cnx.commit()
    

cnx.close()