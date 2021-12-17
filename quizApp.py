#imports
import sys
import csv
import random
import pandas as pd
import glob

quizCategory = "General Knowledge"
questionList = []

#correct check
def mark(panswer, canswer): #this function evluates if the answer is correct 
    if canswer.lower() == panswer.lower():  #if correct answer is same as users answer
        return "correct"
    else:
        return "incorrect"

#turn csv into nested list of questions e.g. [[q,a],[q,a],[q,a]]
def createQList(reader): #recieves csv
    for row in reader: #loop through each row and make a list of questions
        question = [row[0],row[1]] #get each question and answer as a list
        questionList.append(question) #nest each list into 1 over all list

#check if there has been a category chosen
if len(sys.argv) > 1 : #category chosen
    quizCategory = str(sys.argv[1]) #record the name of the category
    with open(f"{sys.argv[1]}.csv", newline='') as f: # open the csv of the chosen category
        reader = csv.reader(f)
        createQList(reader)

else: #no category chosen
    path = r'C:\Users\danie\Desktop\Python training\quizApp' #sets path to location of csv files
    all_files = glob.glob(path + "/*.csv") #creates list of csv files

    for filename in all_files: #for each file
        with open(filename, newline='') as f: #open the csv
            reader = csv.reader(f)
            createQList(reader) #send csv to function to be made into a list

#print a description of how the app works
print("Welcome to the quiz!\n")
numberOfQuestions = input("How many questions would you like? ")
print(f"You have chosen to do the {quizCategory} quiz. Good Luck!\n")

shuffledQuestions = random.sample(questionList, int(numberOfQuestions)) #selects a random number of questions chosen by numberOfQuestions variable 

right = 0

for question in shuffledQuestions.copy(): #for each question in the list of selected questions and answers
    print(question[0]) #print out the question part to the user
    playerAnswer = input("") #request an input from the user
    result = mark(playerAnswer, question[1]) #call the evaluator function to check if question is correct
    print(result) #print the return of mark()

    #add up correct points
    if "in" not in result: #if the word is returned is "correct"
        right += 1 # add a point to right

percent = round((right / int(len(shuffledQuestions)))* 100, 2)

print(f"You got {right} questions right out of {len(shuffledQuestions)}. Thats {percent}%" )
