import sys 
import mysql.connector as sql 
conn=sql.connect(host='localhost',user='root',password='database') 
cur=conn.cursor() 
cur.execute("create database dental_management_system") 
print("Database created succefully")
conn.commit()
conn=sql.connect(host='localhost',user='root',password='database',database='dental_management_system')
if conn.is_connected():
    print("Connection Successfully Established. . . " )
else:
    print("Some Connectivity Issue. . . " )
cur=conn.cursor()
cur.execute("create table patient_record( Patient_Name varchar(50),\
Age int(3),\
Doctor_Conculted varchar(50),\
Address varchar(150),\
Phone_Number bigint(15)") 
cur.execute("create table salary_record( Employee_Name varchar(50),\
Profession varchar(20),\
Salary_Amount varchar(9),\
Address varchar(150),\
Phone_Number bigint(15)") 
cur.execute("create table accounts(User_Name varchar(20) primary key,\
password varchar(30) unique)") 
print("Tables created successfully") 
conn.commit() 
User_Name=input("Enter New User Name : ") 
User_Name=User_Name.upper() 
password=input("Enter New Password : ") 
password=password.upper() 
query=" Insert into accounts values ( '{ }','{ }') ".values(User_Name,password)
print("ACCOUNT ADDED SUCCEFULLY") 
conn.commit() 
if conn.is_connected: 
    print(" Dental Management System ") 
    print("1. Login") 
    print("2. Exit") 
    print() 
    option=int(input("Enter your choice : ")) 
    if option==1: 
        print() 
        User_Name=input('User Name : ') 
        user=user.upper() 
        cur.execute("select * from accounts where User_Name like ' ' ") 
        datas=cur.fetchall() 
        for i in datas: 
            value_1=i[0] 
            value_2=i[1] 
        if User_Name==value_1: 
            password=input('Password : ') 
            password=password.upper() 
            if password==value_2: 
                print() 
                print('Login succefull') 
                print() 
                print("1. Add Patients records") 
                print("2. Add Salary records") 
                print("3. Veiw Patient Detail") 
                print("4. Delete patient detail") 
                print() 
                choice=int(input('Enter a option : ')) 
                if choice==1: 
                    print() 
                    name=input('Name : ') 
                    name=name.upper() 
                    age=input('Age : ') 
                    doc=input('Doctor Consulted : ') 
                    doc=doc.upper() 
                    add=input('Address : ') 
                    add=add.upper() 
                    phone_no=(input('Phone Number : ')) 
                    query=" Insert into patient_record values ( '{ }', { }, { }, '{ }', '{ }', { } ) ".values(name,age,doc,add,phone_no)
                    cur.execute(query)
                    conn.commit() 
                    print('Record added') 
                if choice==2: 
                    print() 
                    emp_name=input( 'Employee_Name : ') 
                    emp_name=emp_name.upper()
                    profession=input('Proffession : ')
                    profession=profession.upper() 
                    salary=int(input('Salary Amount : '))
                    add=('Address : ') 
                    add=add.upper() 
                    phone_no=int(input( 'Phone_Number : ')) 
                    query=" Insert into salary_record values ( '{ }', '{ }', { }, '{ }', { } ) ".values(emp_name,profession,salary,add,phone_no)
                    cur.execute(query)
                    conn.commit() 
                    print('Record added') 
                if choice==3: 
                    print() 
                    name=input('Name of the patient : ') 
                    name=name.upper() 
                    cur.execute("select * from patient_record where patient_name like name ' ' ") 
                    data=cur.fetchall() 
                    if data!=0: 
                        for row in data: 
                            print() 
                            print("Patient Details : ") 
                            print() 
                            print('Name : ',row[0]) 
                            print('Age : ',row[1]) 
                            print('Doctor consulted : ',row[2]) 
                            print('Address : ',row[3]) 
                            print('Phone Number : ',row[4]) 
                            input() 
                    else: 
                        print() 
                        print("Patient Record Doesnot Exist")
                    if choise==4:
                        print()
                        name=input('Name of the patient : ')
                        name=name.upper()
                        cur.execute("delete from patient_record where patient_name like ' ' ")
                        print('Record Deleted Succefully')
                    else:
                        print('Invalid Password')
                        print('Tryagain') 
                elif option==2:
                    sys.exit() 
conn.commit() 
input()       
