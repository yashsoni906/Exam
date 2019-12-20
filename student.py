import login
import csv

#import pdb; pdb.set_trace()
def exam():
	print("welcome to exam")
	answer = input("Are you ready to take the exam? ")

	if answer == 'yes':
	    from admin import questions

	    questions()
	    #from admin import answers
	    #answers()
	    #answer = input("Enter your answer : ")
	    #if answer == 'c':
	    	#result = result + 1
	    	#print("Your result is ", result)
	    #else:
	    	#print("Your result is ", result)

	elif answer == 'no':
	    print("You have chosen no.")

	else:
		print("Invalid input ")
exam()