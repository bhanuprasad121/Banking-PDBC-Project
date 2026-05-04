from db_connection import mysql_connection
import random

conn = mysql_connection()
curobj = conn.cursor()


def add_customer():
    # acc_id = int(input('Enter Account Id: '))
    # customer_name = input('Enter Name: ')
    # age = int(input('Enter Age: '))
    # city = input('Enter City Name: ')
    # balance = float(input('Enter Initial Balance: '))
    # username= input('Enter username: ')
    # password = input('Enter Password: ')
    names=["ravi","poojitha","shirisha","rajiv","mallesh","saxena","akkshay"]
    cities=["Mumabi","Vizag","sholapur","chambal","texas","waynad","tokyo"]
    for acc_id in range(2001,2201):
        customer_name=random.choice(names)+ " "+random.choice(["kumar","sharma","patel","kishan","jeff","jenny","subbu","malika"])
        age=random.randint(21,67)
        city=random.choice(cities)
        balance=random.randint(3000,150000)
        username= "user"+ str(acc_id)
        password= "pass"+str(acc_id)

        query ="""insert into customers
                (acc_id,customer_name,age,city,balance,username,password)
                values(%s,%s,%s,%s,%s,%s,%s)"""

        curobj.execute(query,(acc_id,customer_name,age,city,balance,username,password))
    conn.commit()


    print('Customer Added Successfully ')
    print("="*50)
    

def customer_delete():
    acc_id = int(input("Enter Account Number:"))
    query = "Delete From customers where acc_id =%s"
    curobj.execute(query,(acc_id,))
    conn.commit()

    if curobj.rowcount>0:
        print("Customer Deleted Scuccessfully")
    else:
        print("Customer Not Found")


def customer_login():
    username = input('Enter name: ')
    password = input('Enter password: ')
    query="""select acc_id,customer_name,age,city,balance from customers
    where username=%s and password=%s"""

    curobj.execute(query,(username,password))
    result=curobj.fetchone()

    if result:
        print("Login Successfully")
        print("="*50)
        print("acc_id:",result[0])
        print("name:",result[1])
        print("age:",result[2])
        print("city",result[3])
        print("balance",result[4])
        print("="*50)
    else:
        print("Invalid Login")

while True:
    print("===Bank System===")
    print("1.Bank Employee")
    print("2.Customer")
    print("3.Delete Customer")
    print("4.Exit")

    choice=int(input("Enter Your Choice: "))

    if choice==1:
        print("1.Add Customer")
        print("2. Back")
        emp_choice=int(input("Enter Choice:"))

        if emp_choice==1:
            add_customer()

        elif emp_choice==2:
            continue

        else:
            print("Invalid choice")            
    elif choice==2:
        customer_login()
    elif choice==3:
        customer_delete()    
    elif choice==4:
        print("Exting...")
        break
    else:
        print("Invalid Choice")    

