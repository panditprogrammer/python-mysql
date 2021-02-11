#creating table with python

import mysql.connector
#now selecting database 
mydatabase = mysql.connector.connect(host='localhost',
                                     user='root',
                                     password='',
                                     database='pythondb')
#for any operation use cursor object
cur = mydatabase.cursor()
#sql command
sql='CREATE TABLE student (name varchar(20),roll int(4),address varchar(20))'
cur.execute(sql)

