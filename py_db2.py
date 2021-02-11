import mysql.connector
#conneting to database
mydatabase = mysql.connector.connect(host='localhost',user='root',password='')
#for any operation use cursor object
cur = mydatabase.cursor()
# sql command 
cur.execute("CREATE DATABASE pythondb")
