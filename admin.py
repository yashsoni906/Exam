import csv 
import hashlib
import getpass
import json
import sys

def info():
    print("Hello Admin")
    #with open('student.csv', newline='')as csvfile:
        #with open('student_hashed.csv', 'w') as newfile:
            #reader = csv.DictReader(csvfile)
            #for i, r in enumerate(reader):
                #newfile.write(','.join(r) + '\n')
                #r['password'] = hashlib.sha256((r['password']).encode('utf-8')).hexdigest()
                #newfile.write(','.join(r.values()) + '\n')
        #spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        #for row in spamreader:
            #print(', '.join(row))

    details = input("Do you want to add details?")
    for yes in details:
        if details == 'yes':
            with open('student_hashed.csv', mode='a')as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting =csv.QUOTE_MINIMAL)
                username=input("Enter Username : ")
                password=getpass.getpass(prompt='Enter password:',stream=None)
                password=hashlib.sha256((password).encode('utf-8')).hexdigest()
                result = 0
                spamwriter.writerow([username, password, result])
                details=input("Add more details?")

        elif details == 'no':
            pass 

        else:
            print("invalid input ")


def questions():
    print(' ')
    result=0
    wanted = ('question', 'option1', 'option2', 'option3', 'option4')
    with open('questions.csv')as csvfile:
        reader = csv.DictReader(csvfile)
        conclusion = []
        for row in reader:
            conclusion.append({k:v for k,v in row.items() if k in wanted})

    for f in conclusion:
        temp1 = json.dumps(f)
        if '[' not in temp1 or ']' not in temp1 or not temp1.strip():
            print("Problem with questions ... Please contact admin")
            sys.exit()

    for r in conclusion:
        temp=json.dumps(r)
        print(r['question'])
        question = r['question']
        option1 = r['option1']
        option2 = r['option2']
        option3 = r['option3']
        option4 = r['option4']
        print("{:<20}".format(option1.replace('[','').replace(']','')),'        ',"{:<20}".format(option2.replace('[','').replace(']','')))
        print("{:<20}".format(option3.replace('[','').replace(']','')),'        ',"{:<20}".format(option4.replace('[','').replace(']','')))
        answer = input("Enter your answer : ")
        
        a = '['+answer+']'
        if a in temp:
            result = result + 1
    print('Your result is : ',result)
    username= input('Enter your username to display result: ')
    with open ('student_hashed.csv','r')as csvinput:
        with open ('result.csv','a')as csvoutput:
            writer = csv.writer(csvoutput)
            for row in csv.reader(csvinput):
                if row[0] == username:
                    writer.writerow(row + [result])
                    #print(','.join(row),'   ,','Result:',result)
                    print(username,'  ,','Result:',result)
#def answers():
    #with open('answers.csv')as csvfile:
        #reader = csv.reader(csvfile, quotechar='|')
        #for row in reader:
            #print(' '.join(row))

#def edit_questions():
    #with open('questions.csv')