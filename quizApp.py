#imports
import sys
import csv
import random
import pandas as pd
import glob

#check to see if anything was entered when code ran in commandline 
#e.g. quizApp.py christmas
#this will filter the questions by genre if none selected import all csv's that are there 

quizCatagory = "General Knowledge"
questionList = []

if len(sys.argv) > 1 : #check if there has been a catagory chosem
    quizCatagory = str(sys.argv[1]) #record the name of the catagory
    with open(f"{sys.argv[1]}.csv", newline='') as f: # open the csv of the chosen catagory
        reader = csv.reader(f)
        for row in reader: #loop through each row and make a list of questions
            question = [row[0],row[1]] #get each question and answer as a list
            questionList.append(question) #nest each list into 1 over all list
else:
    # path = r'C:\Users\danie\Desktop\Python training\quizApp'
    # all_files = glob.glob(path + "/*.csv")

    # li = []

    # for filename in all_files:
    #     df = pd.read_csv(filename)
    #     li.append(df)
    # print(li)

    path = r'C:\Users\danie\Desktop\Python training\quizApp'
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename)
        li.append(df)
    print(li)



#print a description of how the app works
print("Welcome to the quiz!\n")
print(f"You have chosen to do the {quizCatagory} quiz. Good Luck!")




#for every row in the csv assigin  column 1 question and column2 answer and append to a list



#pick randomly pick from the list of questions and request user input


#send user input + q + a into a function that assesses if the answer is correct and adds 1 to a correct or wrong answers tally


#when there are no more questions return the number of correct answers, wrong answers and % of correct 

