# random_quiz.py - creates 35 unique quizzes
# - Creates 50 multiple-choice questions for each quiz, in random order
# - Provides the correct answer and three random wrong answers for each question,
#   in random order.
# - Writes the quizzes to 35 text files.
# - Writes the answer keys to 35 text files.

import os  # to create folders and manipulate files
import random  # to shuffle and randomise questions and answers

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':'Augusta',
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing',
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 unique quiz files
for i in range(35):
    # Create quiz and answer key files
    quiz_file = open('quiz_questions%s.txt' % i+1), 'w')  # current directory, create new path for each quiz
    answers_file= open('quiz_answers%s.txt' % i+1), 'w')
    
    # Write out header for the quiz
    quiz_file.write('Name:\n\nDate\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + 'State Capitals Quiz (Form %s)' % i+1)
    quiz_file.write('\n\n')

    # Shuffle order of the states
    states = list(capitals.keys())
    random.shuffle(states)

# Creating the Multiple Choice Answers
# Now we loop through the states and get their correct values using the dict
for i in range(50):  # looping through all 50 states
    # Fetch right and wrong answers
    correct_answers = capitals[states[i]]
    wrong_answers = list(capitals.values())
    del wrong_answers[i]  # remove the correct answer

    # RANDOM
    correctAnswer = capitals[states[questionNum]]
    WrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)

    # Write the question and the answer options to the quiz file.
    quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
    for i in range(4):
        quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')
        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()

    # loop through all 50 states, generating a question for each
    
