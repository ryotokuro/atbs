# random_quiz.py
# Creates 35 different quizzes.
# - Creates 50 multiple-choice questions for each quiz, in random order
# - Provides the correct answer and three random wrong answers for each question,
#   in random order.
# - Writes the quizzes to 35 text files.
# - Writes the answer keys to 35 text files.

import os  # to create folders and manipulate files
import random  # to shuffle and randomise questions and answers

answers = {
            'Name of Kanye\'s first child?': 'North West',
            'Kanye\'s favourite restaurant is: ': 'McDonalds',
            'Kanye\'s first album was titled :': 'The College Dropout',
            'Kanye\'s first public celebrity relationship was with whom?': 'Amber Rose',
            'What is Kanye\'s middle name?': 'Omari',
            'What is the name of Kanye\'s charity organisation?': 'Donda',
            'Which albums feature the iconic bear in the album cover?':'College Dropout, Graduation',
            'What is Kanye West\'s most played radio hit?':'No ID'
            }

