import csv
import getpass
import hashlib 
import sys
answer = input("Welcome to exam! Do you have an account? yes or no : ")


logIn = False

if answer == 'yes':
    csvfile = open('student_hashed.csv')
    reader = csv.reader(csvfile)
    username = input("Username:")
    for row in reader:
        if row[0] == username:
            password = getpass.getpass(prompt='Password:', stream=None)
            password = hashlib.sha256((password).encode('utf-8')).hexdigest()
            if row[1] == password:
                logIn = True
                print(" You're now logged in")
                if username == 'admin':
                    #print("Hello admin")
                    from admin import info
                    info()
                    sys.exit("Thank you admin")
            elif row[1] != password:
                sys.exit("Incorrect Password")

elif answer == 'no':
    #print("Please Contact Admin ") 
    sys.exit("Plese Contact Admin")

if logIn == False:
    sys.exit("Invalid Credentials Please Contact admin for support")
