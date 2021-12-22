import glob
import csv
import random

#Locates the csv files that hold questions
path = r'C:\Users\Ewen\Desktop\quizApp' #sets path to location of csv files
all_files = glob.glob(path + "/*.csv") #creates list of csv files

#Formats the filenames for output
def formatFilenames():
    for file in all_files:
        print(file.replace(".csv", "").replace(path + "\\", ""))

#Creates the question list
def createQuestionList(readerInput):
    questionList = []
    for row in readerInput: #loop through each row and make a list of questions
        question = [row[0],row[1]] #get each question and answer as a list
        questionList.append(question) #nest each list into 1 over all list
    return questionList


#returns question list filtered by category, if not uses general knowledge
def categoryCheck(quizCategoryInput):

    qlistCat = []
    
    if quizCategoryInput == "" or any(quizCategoryInput in sublist for sublist in all_files) == False:
        quizCategoryInput = "General Knowledge"
        for file in all_files: #take all available questions from all files
            with open(file, newline='') as f:
                reader = csv.reader(f)
                qlistCat.extend(createQuestionList(reader))

    else: #if the chosen category is on the list of CSVs
        with open(f"{quizCategoryInput}.csv", newline='') as f: #Create a list of questions from that category
            reader = csv.reader(f)
            qlistCat = createQuestionList(reader)

    return [qlistCat, quizCategoryInput] #return the categorized list and the value of category input


#Marks to check the answers are correct are not
def mark(playerAnswer, AnswerFromList): #this function evaluates if the answer is correct 
    if AnswerFromList.lower() == playerAnswer.lower():  #if correct answer is same as users answer
        return 1 #"Correct"
    else:
        return 0 #"Incorrect"


#Shuffles the list of questions
def shuffledQuestions(questionNumber, categorizedList):
    shuffledQuestions = random.sample(categorizedList, int(questionNumber)) #selects a random number of questions chosen by numberOfQuestions variable 
    return shuffledQuestions


#Asks the questions, waits for input and prints result by calling mark function
def questionAsker(questionFromList):
    print(questionFromList[0])
    playerAnswer = input("")
    result = mark(playerAnswer, questionFromList[1])
    return result


#Starts asking questions and provides correct answer if wrong anwer given, counts number of correct answers
def quizStart(finishedList):
    numCorrect = 0
    for question in finishedList:
        result = questionAsker(question)
        if result == 0:
            print(f"Incorrect! {question[1]} was the correct answer.\n")
        else:
            print("Correct! good work!\n")
            numCorrect += 1
    return numCorrect

#returns a percentage based on your final score
def showScore(numCorrect, finishedListLength):
    percent = round((numCorrect / finishedListLength)* 100, 2) #creates a right/wrong %
    return [percent, numCorrect]

#Take an input, make sure it is the correct expected input, true if so false if not
def userInputSanitizer(input, type):
    
        return True

        return False