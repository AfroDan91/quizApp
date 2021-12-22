#imports
import csv
import random
import glob

quizCategory = ""
questionList = []


#print a description of how the app works
print("Welcome to the quiz!\n")

path = r'C:\Users\danie\Desktop\Python training\quizApp' #sets path to location of csv files
all_files = glob.glob(path + "/*.csv") #creates list of csv files

print(f"There are {len(all_files)} categories to choose from, they are:")


for file in all_files:
    print(file.replace(".csv", "").replace(path + "\\", "")) #prints the names of the .csv minus the directory path

print("General Knowledge")
quizCategory = input("to choose a category type its name here -> ")

def createQuestionList(reader): #creates a question list from selected .csv
    for row in reader: #loop through each row and make a list of questions
        question = [row[0],row[1]] #get each question and answer as a list
        questionList.append(question) #nest each list into 1 over all list

#check if chosen category has a .csv file
if quizCategory in all_files: #if it is
    with open(f"{quizCategory}.csv", newline='') as f: # open the csv of the chosen category
        reader = csv.reader(f)
        createQuestionList(reader) #turn it into a question list
else: #if not
    quizCategory = "General Knowledge"
    for filename in all_files: #take all available questions
        with open(filename, newline='') as f: #open the csv
            reader = csv.reader(f)

            createQuestionList(reader) #turn them into a question list

numberOfQuestions = input(f"There are {len(questionList)} questions in that category, how many {quizCategory} questions would you like to do? ")
print(f"You have chosen to do {numberOfQuestions} in the {quizCategory} category. Good Luck!\n")

def mark(panswer, canswer): #this function evaluates if the answer is correct 
    if canswer.lower() == panswer.lower():  #if correct answer is same as users answer
        return "Correct"
    else:
        return "Incorrect"
      
shuffledQuestions = random.sample(questionList, int(numberOfQuestions)) #selects a random number of questions chosen by numberOfQuestions variable 

right = 0

for question in shuffledQuestions.copy(): #for each question in the randomized list of questions
    print(question[0]) #ask the question
    playerAnswer = input("") #take the users answer
    result = mark(playerAnswer, question[1]) #check if given answer is correct
    print(result) #print if the answer is correct or not
    if "In" not in result:
        right += 1
    else:
        print(f"The correct answer was: {question[1]}\n")

percent = round((right / int(len(shuffledQuestions)))* 100, 2) #creates a right/wrong %

print(f"You got {right} questions right out of {len(shuffledQuestions)}. Thats {percent}%" )
