#imports
import sys
import csv
import random
import pandas as pd
import glob

quizCategory = "General Knowledge"
questionList = []

 #check if there has been a category chosen
if len(sys.argv) > 1 : #category chosen
    quizCategory = str(sys.argv[1]) #record the name of the category
    with open(f"{sys.argv[1]}.csv", newline='') as f: # open the csv of the chosen category
        reader = csv.reader(f)
        for row in reader: #loop through each row and make a list of questions
            question = [row[0],row[1]] #get each question and answer as a list
            questionList.append(question) #nest each list into 1 over all list
    print(questionList)

else: #no category chosen
    path = r'C:\Users\danie\Desktop\Python training\quizApp' #sets path to location of csv files
    all_files = glob.glob(path + "/*.csv") #creates list of csv files

    for filename in all_files: #for each file
        with open(filename, newline='') as f: #open the csv
            reader = csv.reader(f)
            for row in reader: #loop through each row and make a list of questions
                question = [row[0],row[1]] #get each question and answer as a list
                questionList.append(question) #nest each list into 1 over all list

def mark(panswer, canswer): #this function evluates if the answer is correct 
    if canswer.lower() == panswer.lower():  #if correct answer is same as users answer
        return "correct"
    else:
        return "incorrect"

#print a description of how the app works
print("Welcome to the quiz!\n")
numberOfQuestions = input("How many questions would you like? ")
print(f"You have chosen to do the {quizCategory} quiz. Good Luck!\n")

shuffledQuestions = random.sample(questionList, int(numberOfQuestions)) #creates a randomised list from all questions in questionList

right = 0
wrong = 0


for question in shuffledQuestions.copy(): 
    print(question[0])
    playerAnswer = input("")
    result = mark(playerAnswer, question[1])
    print(result)
    if "in" in result:
        wrong += 1
    else:
        right += 1
percent = round((right / int(len(shuffledQuestions)))* 100, 2)

print(f"You got {right} questions right out of {len(shuffledQuestions)}. Thats {percent}%" )
