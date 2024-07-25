#! python3

import os
import pyinputplus
from pathlib import Path
import random

# Quiz Data:
quizQuestionsAndAnswers = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford','Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate a number of quiz files:
quizOutputFileLocation = Path.cwd() / "Files" / "Quizzes"
quizCount = pyinputplus.inputNum("How many quiz and answer key combos should be generated\n> ", min=1, limit=1, default=10)

for currentQuizNumber in range(quizCount):
    quizFile = Path(quizOutputFileLocation / f"CapitalsQuiz{currentQuizNumber +1}.txt")
    answerKeyFile = Path( quizOutputFileLocation / f"CapitalsQuiz_AnswerKey{currentQuizNumber + 1}.txt")
    print(quizFile)
    print(answerKeyFile)

# Loop through the available answer combinations, creating questions for each:

#   Get correct and incorrect options:

#    Write the question and answer options to the quiz file:

#    Write answer key to a file:
