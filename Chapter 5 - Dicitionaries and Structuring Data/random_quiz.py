# random_quiz.py - creates 35 unique quizzes
# - Creates 50 multiple-choice questions for each quiz, in random order
# - Provides the correct answer and three random wrong answers for each question,
#   in random order.
# - Writes the quizzes to 35 text files.
# - Writes the answer keys to 35 text files.

import os  # to create folders and manipulate files
import random  # to shuffle and randomise questions and answers

'''
    'Name of Kanye\'s first child?': 'North West',
    'Kanye\'s favourite restaurant is: ': 'McDonalds',
    'Kanye\'s first album was titled :': 'The College Dropout',
    'Kanye\'s first public celebrity relationship was with whom?': 'Amber Rose',
    'What is Kanye\'s middle name?': 'Omari',
    'What is the name of Kanye\'s charity organisation?': 'Donda',
    'Which albums feature the iconic bear in the album cover?':'College Dropout, Graduation',
    'What is Kanye West\'s most played radio hit?':'No ID'
'''
answers = {
            # The College Dropout
            "Intro": "The College Dropout",
            "We Don't Care": "The College Dropout",
            "Graduation Day": "The College Dropout",
            "All Falls Down": "The College Dropout",
            "I'll Fly Away": "The College Dropout",
            "Spaceship": "The College Dropout",
            "Jesus Walks": "The College Dropout",
            "Never Let Me Down": "The College Dropout",
            "Get Em High": "The College Dropout",
            "Workout Plan": "The College Dropout",
            "The New Workout Plan": "The College Dropout",
            "Slow Jamz": "The College Dropout",
            "Breathe In Breath Out": "The College Dropout",
            "School Spirit (Skit 1)": "The College Dropout",
            "School Spirit": "The College Dropout",
            "School Spirit (Skit 2)": "The College Dropout",
            "Lil' Jimmy": "The College Dropout",
            "Two Words": "The College Dropout",
            "Through the Wire": "The College Dropout",
            "Family Business": "The College Dropout",
            "Last Call": "The College Dropout",
            # Late Registration
            "Wake Up Mr. West": "Late Registration",
            "Heard 'Em Say": "Late Registration",
            "Touch the Sky": "Late Registration",
            "Gold Diggger": "Late Registration",
            "Skit #1": "Late Registration",
            "Drive Slow": "Late Registration",
            "My Way Home": "Late Registration",
            "Crack Music": "Late Registration",
            "Roses": "Late Registration",
            "Bring Me Down": "Late Registration",
            "Addiction": "Late Registration",
            "Skit #2": "Late Registration",
            "Diamonds From Sierra Leone": "Late Registration",
            "We Major": "Late Registration",
            "Skit #3": "Late Registration",
            "Hey Mama": "Late Registration",
            "Celebration": "Late Registration",
            "Skit #4": "Late Registration",
            "Gone": "Late Registration",
            "Late": "Late Registration",
            "Back to Basics": "Late Registration",
            "We Can Make it Better": "Late Registration",
            # Graduation
            "Good Morning": "Graduation",
            "Good Morning": "Graduation",
            "Champion": "Graduation",
            "Stronger": "Graduation",
            "I Wonder": "Graduation",
            "Good Life": "Graduation",
            "Can't Tell Me Nothing": "Graduation",
            "Barry Bonds": "Graduation",
            "Drunk and Hot Girls": "Graduation",
            "Flashing Lights": "Graduation",
            "Everything I am": "Graduation",
            "The Glory": "Graduation",
            "Homecoming": "Graduation",
            "Big Brother": "Graduation",
            "Good Night": "Graduation",
            "Bittersweet Poetry": "Graduation",
            # 808s & Heartbreak
            "": "Graduation",
            "": "Graduation",
            "": "Graduation",
            "": "Graduation",
            "": "Graduation",
            
          }

# generate 35 unique quiz files
for i in range(35):
    # create quiz and answer key files
    os.path('.' + str(i))  # current directory, create new path for each quiz

    # write out header for the quiz

    # shuffle order of the states

    # loop through all 50 states, generating a question for each
