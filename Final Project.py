#Final Project Implementation by Ye Eun Lee
#As a note, my main program code (section 'Main program') does not function properly when
#defined as function main(), but outside of this it works without error. I spent a considerable
#amount of time attempting to troubleshoot this, but was unable to resolve the error.

import random

#Define functions
def quizQuestions(n, states):
    """Produces an ordered list of n random states to quiz from list states"""
    if n > 12:
        select = random.sample(states, 12)
        return select
    else:
        random.shuffle(states)
        return states

def checkAnswer(state, useranswer):
    """Compares user's input answer with the correct dictionary answer"""
    if useranswer == scpair[state]:
        return True
    else:
        return False
def answerKey(file, questions):
    """Produces a dictionary answer key of states and their capitals, given a file and its size"""
    capitalsDict = {}
    for i in range(0, questions):
        pair = file.readline()
        pair = pair.rstrip('\n')
        state, capital = pair.split(', ')
        capitalsDict[state] = capital
    return capitalsDict
def percentCorrect(numCorrect, total):
    """Calculates the percentage of answers correctly answered"""
    raw = numCorrect/total
    raw *= 100
    rounded = round(raw)
    percent = str(rounded)
    return percent

#Main program
#Prompt user for file location and name
location = str(input('Please input the location of the quiz file, starting with C:\ and ending with .txt \n'))
    
#Read contents of file
infile = open(location, 'r')
questions = sum(1 for line in infile)
infile.close()
    
#Create dictionary of state-capital pairings
infile = open(location, 'r')
scpair = answerKey(infile, questions)
infile.close()

#Establish list of states for reference
states = list(scpair.keys())
    
#User interface
print('Welcome to the capitals quiz! \n' +
    'This quiz will ask for the capitals of several states.')
    
questionList = quizQuestions(questions, states) #make list permanent so function doesn't recall a new list every time

correct = 0 #keep count of questions correct for scoring
    
for qstate in questionList:
    answer = input('What is the capital of ' + qstate + '?  ')
    if checkAnswer(qstate, answer) == True:
        print('\nYou got it! Next question: \n')
        correct += 1
    else:
        print("\nSorry, that's not it! The capital of " + qstate + " is " + scpair[qstate] + ". \n")


print('Congratulations! You got ' + str(correct) + ' correct out of ' + str(len(questionList)) + ". \nThat's " +
      percentCorrect(correct, len(questionList)) + '%!')
        
    
    
    
        
    
