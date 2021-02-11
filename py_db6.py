#Extracting data from table with python

import mysql.connector
#conneting to database and select
mydatabase = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='pythondb')
#for any operation use cursor object
cur = mydatabase.cursor()
#sql command
sql="SELECT * FROM student"
cur.execute(sql)
#getting result from database in the form of tuple
result = cur.fetchall()
for record in result:
    print(record)


