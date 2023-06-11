
import mysql.connector as sql
mydb = sql.connect(host ='localhost',port='3306',user ='root',passwd ='1234',database ='ccms')
if mydb.is_connected():
    print("successfully connected")
c1=mydb.cursor()

print("                           ****************SMART TECH INTERNET CAFE WELCOMES YOU****************        ")
print("  \n                                            ___CYBER CAFE MANAGEMENT SYSTEM___            ")

print("Access type")
print("1.Owner")
print("2.Customer")
choice=int(input("Your Answer (1 or 2):"))
if choice==1:
    pw=int(input("Enter Password:"))
    if pw==2809:
        while True:
            print("\n")
            print("1.Customers Detailed view")
            print("2.Bill Details")
            print("3.Generate Bill")
            print("4.Exit")
        
            a=int(input("Enter Your Choice:"))
            if a==1:
                ea="select * from Add_new_customer"
                c1.execute(ea)
                data=c1.fetchall()
                print("{:<10} {:<4} {:<15} {:<10} {:<9}".format("NAME","AGE","ADDRESS","PHONE NO.","EMAIL ID"))
                for row in data:
                    print("{:<10} {:<4} {:<15} {:<10} {:<9}".format(row[0],row[1],row[2],row[3],row[4]))
            elif a==2:
                ea="select * from bill"
                cl=mydb.cursor()
                cl.execute(ea)
                data=cl.fetchall()
                print("{:<10} {:<22} {:<10}".format("NAME","TIME ACCESSED(IN MIN)","TOTAL CHARGES"))
                for row in data:
                     print("{:<10} {:<22} {:<10}".format(row[0],row[1],row[2]))
            elif a==3:
                name=input("Enter Name :")
                time=input("Enter the time :") 
                amount=int(input("Enter the amount :"))
                ss="insert into bill values('{}',{},{})".format(name,time,amount)
                c1.execute(ss)
                mydb.commit()
                print("Bill Generated")
            elif a==4:
                print("                                                THANK YOU VISIT AGAIN               ")
                break
            else:
                print("Invalid choice")
    else:
        print("Wrong password entered")
        print("Program Stopped")
elif choice==2:

    while True:
        print("\n")
        print("1.New Customer")
        print("2.View Bill")
        print("3.Exit")
        a=int(input("Enter your choice :"))
        if a==1:
            name=input("Enter your name :")
            age=int(input("Enter your age :"))
            address=input("Enter your residential address :")
            phone_no=int(input("Enter your phone number :"))
            email_id=input("Enter your Email ID :")
            ty="insert into Add_new_customer values('{}',{},'{}',{},'{}')".format(name,age,address,phone_no,email_id)
            c1.execute(ty)
            mydb.commit()
            print("Data added......")
        elif a==2:
            name=input("Enter Your Name :")
            
            ea="select * from bill where customer_name='{}'".format(name)
            c1.execute(ea)
            data=c1.fetchall()
            for row in data:
                print("Name                :",row[0])
                print("Total time( in min) :",row[1])
                print("Total Amount        :",row[2])
        elif a==3:
            print("                                                THANK YOU VISIT AGAIN               ")
            break
        else:
            print("Invalid choice...")

else:
    print("Invalid Choice...")


            






    
