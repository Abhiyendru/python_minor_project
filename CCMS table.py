import mysql.connector as sql
mydb = sql.connect(host ='localhost',port='3306',user ='root',passwd ='1234')
if mydb.is_connected():
    print("successfully connected")
c1=mydb.cursor()
c1.execute('create database ccms')
c1.execute('use ccms')
c1.execute('create table Add_new_customer(Customer_name varchar(20),\
Age int,Address varchar(100),Phone_no int(10),Email_ID varchar(30))')
c1.execute('create table Bill(Customer_name varchar(20),\
Time_accessed_in_min int,Total_charges int)')

print("Table created")
