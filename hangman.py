# This is a simple hangman game and there are 10 questions.

"""
After each question, in brackets, there is a hint that let's player the expected output
The game records the number of questions you have answered wrong.
If you fail a question, the program responds with "You are hanging the man\n"
After six mistakes game is lost and stops
You get the message "You have hanged the man\n"
If you finish the game
you get "you're done (insert name), you reached the end and only made x mistake/s"
"""
# Create dictionary that contains each question and the correct answer to which I can refer.
answers_dict = {'When was ALU founded?': 2015,
                'Who is the CEO of ALU?': 'Fred Swaniker',
                'Where are ALU campuses?': 'Rwanda and Mauritius',
                'How many campuses does ALU have?': 2,
                'What is the name of ALU Rwanda’s Dean?': 'Gaidi Faraj',
                'Who is in charge of Student Life?': 'Sila Ogidi',
                'What is the name of our Lab?': 'Nigeria',
                'How many students do we have in Year 2 CS?': 57,
                'How many degrees does ALU offer?': 8,
                'Where are the headquarters of ALU?': 'Mauritius'}
# First we get the player's name
player_name = input('Hello and welcome to hangman by Aimar, what is you name? ')

# Then we give the user a set of instructions that explains the game and the expected input.
print(f'''
Hi {player_name}, lets see how well you know ALU
The game is very simple, you will first see a question and in brackets is the expected answer. 
As an example:
For (Year) give the year in numbers i.e 2010  
For (Full Name) give the full name and capitalize the first letters i.e Aimar Cyusa
Nothing difficult right, have fun!!
''')

# Ask if the user wants to play
start_game = input('Do you want to start playing? yes or no: ')
# Start game. Game will run if start game starts with y
while start_game.lower().startswith('y'):
    WRONG_ANSWERS = 0  # Variable that holds number of wrong answers
    user_input = int(input('When was ALU founded? '))  # Ask  question and save answer
    if user_input in answers_dict.values():  # Check if users answer in all correct answers
        print('well done\n')
    else:   # If there is no answer
        WRONG_ANSWERS += 1  # First we add one to the wrong answers count
        if WRONG_ANSWERS == 6:  # Check if we have not reached the total
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')  # If not print hanging the man

    user_input = input('Who is the CEO of ALU? ')
    # There are two possible answers; Fred Swaniker or Swaniker Fred
    # Lower and split correct answer at the space and save each name as first and last name
    first_name, last_name = (answers_dict['Who is the CEO of ALU?']).lower().split()
    # Convert the player's response and split at the space to create a list of user answers
    user_answers = user_input.lower().split()
    # Check whether real first and last names are in our user_answers list
    if first_name and last_name in user_answers:
        print('well done\n')
    else:  # If they are not
        WRONG_ANSWERS += 1  # Add 1 to our wrong answers count
        if WRONG_ANSWERS == 6:  # Check if we have not reached the total
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')  # If not then print hanging the man

    user_input = input('Where are ALU campuses? ')
    first_campus, second_campus = (answers_dict['Where are ALU campuses?']).lower().split(' and ')
    user_answers = user_input.lower().split()
    if first_campus and second_campus in user_answers:
        print('well done\n')
    else:
        WRONG_ANSWERS += 1
        if WRONG_ANSWERS == 6:
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')

    user_input = int(input('How many campuses does ALU have? '))
    if user_input in answers_dict.values():
        print('well done\n')
    else:
        WRONG_ANSWERS += 1
        if WRONG_ANSWERS == 6:
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')

    user_input = input('What is the name of ALU Rwanda’s Dean? ')
    first_name, last_name = (answers_dict['What is the name of ALU Rwanda’s Dean?']).lower().split()
    user_answers = user_input.lower().split()
    if first_name and last_name in user_answers:
        print('well done\n')
    else:
        WRONG_ANSWERS += 1
        if WRONG_ANSWERS == 6:
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')

    user_input = input('Who is in charge of Student Life? ')
    first_name, last_name = (answers_dict['Who is in charge of Student Life?']).lower().split()
    user_answers = user_input.lower().split()
    if first_name and last_name in user_answers:
        print('well done\n')
    else:
        WRONG_ANSWERS += 1
        if WRONG_ANSWERS == 6:
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')

    user_input = input('What is the name of our Lab? ')
    if user_input in answers_dict.values():
        print('well done\n')
    else:
        WRONG_ANSWERS += 1
        if WRONG_ANSWERS == 6:
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')

    user_input = int(input('How many students do we have in Year 2 CS? '))
    if user_input in answers_dict.values():
        print('well done\n')
    else:
        WRONG_ANSWERS += 1
        if WRONG_ANSWERS == 6:
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')

    user_input = int(input('How many degrees does ALU offer? '))
    if user_input in answers_dict.values():
        print('well done\n')
    else:
        WRONG_ANSWERS += 1
        if WRONG_ANSWERS == 6:
            print('You have hanged the man\n')
            break
        print('You are hanging the man\n')

    user_input = input('Where are the headquarters of ALU? ')
    if user_input in answers_dict.values():
        print('well done\n')

    else:
        print('You are hanging the man\n')
        WRONG_ANSWERS += 1

    # If player reaches the end of the
    # Print congratulatory statement
    # Include the number of wrong answer's they may have had
    # For the sake of english correctness, If we have one mistake prints ...only made 1 mistake
    # Otherwise print ...only make x mistakes. x!=0
    if WRONG_ANSWERS == 1:
        print(f"\nwell done\n {player_name}, you're done and only made {WRONG_ANSWERS} mistake")
    else:
        print(f"\nwell done\n{player_name}, you're done and only made {WRONG_ANSWERS} mistakes")

    break
