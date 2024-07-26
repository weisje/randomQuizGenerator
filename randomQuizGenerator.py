#! python3

import os
import pyinputplus
from pathlib import Path
import random

# Quiz Data:
quizQuestionsAndAnswers = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate a number of quiz files:
quizOutputFileLocation = Path.cwd() / "Files" / "Quizzes"
quizCount = pyinputplus.inputNum("How many quiz and answer key combos should be generated\n> ", min=1, limit=3, default=10)

for currentQuizNumber in range(quizCount):
    quizFilePath = Path(quizOutputFileLocation / f"CapitalsQuiz{currentQuizNumber + 1}.txt")
    answerKeyFilePath = Path(quizOutputFileLocation / f"CapitalsQuiz_AnswerKey{currentQuizNumber + 1}.txt")

    quizFile = open(quizFilePath, 'w')
    answerKeyFile = open(answerKeyFilePath, 'w')

    quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {currentQuizNumber + 1})')
    quizFile.write('\n\n')

    quizKeyShuffle = list(quizQuestionsAndAnswers.keys())
    random.shuffle(quizKeyShuffle)

# Loop through the available answer combinations, creating questions for each:

#   Get correct and incorrect options:
    for questionNum in range(len(quizQuestionsAndAnswers)):
        correctAnswer = quizQuestionsAndAnswers[quizKeyShuffle[questionNum]]
        wrongAnswers = list(quizQuestionsAndAnswers.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

#   Write the question and answer options to the quiz file:
        quizFile.write(f"{questionNum + 1}. What is the capital of {quizKeyShuffle[questionNum]}?\n")
        for i in range(4):
            quizFile.write(f"\t{'ABCD'[i]}. { answerOptions[i]}\n")
        quizFile.write('\n')

#   Write answer key to a file:
        answerKeyFile.write(f'{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n')
    quizFile.close()
    answerKeyFile.close()
