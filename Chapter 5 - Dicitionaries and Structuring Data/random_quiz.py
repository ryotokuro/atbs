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
            "Heartless": "808s & Heartbreak",
            "Coldest Winter": "808s & Heartbreak",
            "Streetlights": "808s & Heartbreak",
            "": "808s & Heartbreak",
            "": "808s & Heartbreak"
          }
'''

'''
answers = {
        'Australia': 'Canberra',
        '
'''

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

# generate 35 unique quiz files
for i in range(35):
    # create quiz and answer key files
    quiz_file = open('capitals_quiz%s.txt' % i+1), 'w')  # current directory, create new path for each quiz
    answers_file= open('quiz_answers%s.txt' % i+1), 'w')
    
    # write out header for the quiz
    quiz_file.write('Name:\n\nDate\n\nPeriod:\n\n')
    quiz_file.write((' '*20) + 'State Capitals Quiz (Form %s)' % i+1)
    quiz_file.write('\n\n')

    # shuffle order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # fetch right and wrong answers
    correct_answers = capitals[states[i]]
    wrong_answers = list(capitals.values())
    del wrong_answers[i]  # remove the correct answer

    # loop through all 50 states, generating a question for each
    
