import mysql.connector
cnx = mysql.connector.connect(user="root", password="mypass",host="127.0.0.1",database="employee")
query= "SELECT * FROM employee ORDER BY Height DESC , Weight ASC;"

cursor = cnx.cursor()

cursor.execute(query)

for (Name, Weight, Height) in cursor:
   
    print("%s %i %i" %(Name,Height,Weight))
   

cnx.close()