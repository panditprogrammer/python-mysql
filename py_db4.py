#inserting data in table with python

import mysql.connector
#connecting to database with and select 
mydatabase = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='pythondb')
#for any operation use cursor object
cur = mydatabase.cursor()
#sql command
sql="INSERT INTO student(name,roll,address) VALUES(%s,%s,%s)"
s1 = ("Rahul",1,"patna") #tuple for placeholder in VALUES
cur.execute(sql,s1)
#To save changes in database
mydatabase.commit()

