from random import choice

answers = ['Undoubtedly!', 'Predetermined!', 'No doubt about it!',
           'Definitely yes', 'You can be sure of it', 'I think so',
           'Most likely!', 'Good prospects', 'The signs say yes',
           'Yes', 'Not clear yet, try again', 'Ask again later',
           "It's best not to tell", "Can't predict now",
           'Concentrate and ask again', "Don't even think about it!",
           'My answer is no', 'Not according to me',
           'Prospects are not very good', 'Very doubtful']

def name_input():
    '''Function for entering a username and checking it for "strangeness"
    '''
    print('''Hi, I'm a magic ball,
          and I know the answer to any question you have!)
          First of all, tell me your name!''')
    name = input()
    if name.isspace() is True:
        print("Oh, my God! I've never seen such spaced people!")
    elif name.isalpha() is not True:
        print('I never knew there were such strange names in the world!')
    else:
        print(f'Hi, {name}')
    return name

name = name_input()

def next_question():
    '''A function requesting the user's
    willingness to ask the following question
    '''
    while True:
        print('''Do you still have any questions for me?
          Enter "y" if yes or "n" if no.''')
        answer = input()
        if answer == 'y' or answer == 'Y':
            return True
        elif answer == 'n' or answer == 'N':
            return False
        else:
            print('My friend, pay attention!')

while True:
    print('Sunshine, ask a question that can be answered yes or no.')
    input()
    print(choice(answers))
    repeat = next_question()
    if repeat is True:
        continue
    else:
        break

print(f"{name}, don't be afraid to contact me if you have any questions!")
print('See you soon!')