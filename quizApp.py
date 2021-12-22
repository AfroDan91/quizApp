#imports
import quizFunctions as qfunc

#print a description of how the app works
print("Welcome to the quiz!\n")

print(f"There are {len(qfunc.all_files)+1} categories to choose from, they are:")

#print a list of all categories
qfunc.formatFilenames()

#print(qfunc.all_files)
print("General Knowledge")

#returns a list of 2 items, question list and quiz category
categorizedList = qfunc.categoryCheck(input("to choose a category type its name here -> "))

#asks the user how many questions they would like to do from total in list
numberOfQuestions = input(f"There are {len(categorizedList[0])} questions in that category, how many {(categorizedList[1])} questions would you like to do? \n")

#forces the number of questions to a valid value if an incorrect input is given
if numberOfQuestions > len(categorizedList[0]) or numberOfQuestions <= 0:
    numberOfQuestions = len(categorizedList[0])
    print(f"You have entered an invalid value, number of questions set to {numberOfQuestions}.\n")
elif type(numberOfQuestions) == str:
    numberOfQuestions = int(float(input(f"There are {len(categorizedList[0])} questions in that category, how many {(categorizedList[1])} questions would you like to do? \n")))

print(f"You have chosen to do {numberOfQuestions} questions in the {(categorizedList[1])} category. Good Luck!\n")

#Shuffle the questions, return the finished list
finishedList = qfunc.shuffledQuestions(numberOfQuestions, categorizedList[0])

quizResults = qfunc.showScore(qfunc.quizStart(finishedList), len(finishedList))

print(f"You got {quizResults[1]} questions right out of {len(finishedList)}. Thats {quizResults[0]}%" )
