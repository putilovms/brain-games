#!/usr/bin/env python3
from . import engine


def play():
    name = engine.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer = 0
    while right_answer < 3:
        result_answer = engine.qestions_game_even()
        if result_answer:
            print('Correct!')
            right_answer += 1
        else:
            print("Let's try again, " + name + "!")
            break
    if right_answer == 3:
        print('Congratulations, ' + name + '!')
