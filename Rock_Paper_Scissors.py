#!/usr/bin/env python3
import random
from os import system, name
from time import sleep

win = 0
loss = 0
tie = 0

def clear():
    if name == 'nt':
        var = system('cls')
    else:
        var = system('clear')

def match(variable):
    if variable.capitalize() == 'R' or variable.upper() == 'ROCK':
        return 'ROCK'
    elif variable.capitalize() == 'P' or variable.upper() == 'PAPER':
        return 'PAPER'
    elif variable.capitalize() == 'S' or variable.upper() == 'SCISSORS':
        return 'SCISSORS'
    elif variable.capitalize() == 'Q' or variable.upper() == 'QUIT':
        return 'QUIT'

print('')

while True:
    print('               _________________________')
    print('              |                         |')
    print('              | ROCK, PAPER, SCISSORS   |')
    print('              |' + str(win) + ' WINS, ' + str(loss) + ' LOSSES, ' + str(tie) + ' TIES |')
    print('              |_________________________|')
    print('')
    cpu = random.choice(['ROCK', 'PAPER', 'SCISSORS'])
    user = match(input('Enter your choice (R)ock, (P)aper, (S)cissors or (Q)uit: '))
    print('')

    if user == 'Q' or user == 'QUIT':
        print('Have a good day!')
        break
    elif user == None:
        print('')
        print('Wrong input! Please enter R for rock, P for paper, S for scissors or Q for quit')
        sleep(3)
        clear()
        continue
    else:
        print(user +  ' versus......')
        sleep(1)
        print(cpu)
        sleep(1)

        if user == cpu:
            print()
            print('It is a Tie!')
            tie += 1
        elif user == "ROCK" and cpu == "PAPER":
            print()
            print ("You Lose!")
            loss += 1
        elif user == "PAPER" and cpu == "SCISSORS":
            print()
            print ("You Lose!")
            loss += 1
        elif user == "SCISSORS" and cpu == "ROCK":
            print()
            print ("You Lose!")
            loss += 1
        else:
            print()
            print ('You win!')
            win += 1

        user = ''
        cpu = ''
        print('')
        sleep(2)
        print('')
        clear()
