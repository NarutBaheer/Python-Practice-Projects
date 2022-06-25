import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random.randint:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
        else:
            print(f'YAyyy, congrats. You\'ve guessed the number {random_number} correctly!!')

guess(10)