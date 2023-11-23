import psycopg2

def getAllStudents():#function to print all student info
    
    cur.execute('SELECT * FROM students')
    for record in cur:
        print (record)

    
def addStudentCall():#function to get the users inputs before adding them to the database
    fName = input("Enter First Name: ")
    lName = input ("Enter Last Name: ")
    email = input ("Enter Email: ")
    date = input ("Enter Date: ")
    addStudent(fName,lName,email,date)

def addStudent(first_name,last_name,email,enrollment_date):#takes the 4 required inputs and attempts to add them to the database
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s , %s , %s , %s)", (first_name,last_name,email,enrollment_date))
        conn.commit()
    except psycopg2.errors.UniqueViolation:#if the email is not unique, then an error message is displayed
        print("Non Unique Email")
    except psycopg2.errors.InvalidDatetimeFormat:#if the user enters an invalid date, an error is displayed
        print ("Invalid Date Format")

def updateStudentEmailCall():#function to get the users inputs before editing the database
    id = input("Enter Student ID: ")
    email = input ("Enter New Email: ")
    updateStudentEmail(id,email)

def updateStudentEmail(student_id, new_email):#takes the id the user put in and the new email and updates that entry
    try:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email,student_id))
        conn.commit()
    except psycopg2.errors.UniqueViolation:#if the email is not unique, then an error message is displayed
        print("Non Unique Email")

def deleteStudentCall():#function to get the users inputs before deleting the entry from the database
    id = input("Enter Student ID: ")
    deleteStudent(id)

def deleteStudent(student_id):#takes the id and removes that entry from the database
    cur.execute("DELETE FROM students WHERE student_id = %s", [student_id])
    conn.commit()

#connects to the database

try:
    conn = psycopg2.connect(
    host= input("Enter Host: "),#localhost
    database= input ("Enter Database: "),#A4
    user= input ("Enter Username: "),#postgres
    password=input ("Enter Password: "))#Order.66
    connected = True
except psycopg2.OperationalError:
    print ("Could not connect, try again")
    exit()

#views the current sql version
cur = conn.cursor()#essentially this is used to make our sql commands
print('PostgreSQL database version:')
cur.execute('SELECT version()')
version = cur.fetchone()
print(version)




#loop for asking the user what they want to test
choice = 0
while choice !=5:
    print("1. Get All Students")
    print("2. Add Student")
    print("3. Edit Student Email")
    print("4. Delete Student")
    print("5. EXIT")
    try:
        choice = int(input("Please enter your choice: "))
        if choice <1 or choice >5:
            print("Enter a number from 1-5")
        elif choice == 1:
            getAllStudents()
        elif choice == 2:
            #addStudent("Matteo", "Carpignano", "email", "2023-01-01")
            addStudentCall()
        elif choice == 3:
            updateStudentEmailCall()
        elif choice == 4:
            deleteStudentCall()
    except ValueError:
        print("ENTER A NUMBER")
        
cur.close()
conn.close()


