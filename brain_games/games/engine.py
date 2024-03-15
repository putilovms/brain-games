#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return (name)


def qestions_game_even():
    number = randint(1, 100)
    answer = prompt.string('Question: ' + str(number) + ' ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    print('Your answer: ' + answer)
    if (answer == correct_answer):
        return True
    print("'yes' is wrong answer ;(. Correct answer was '"
          + correct_answer + "'.")
    return False
