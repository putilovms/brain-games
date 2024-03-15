#!/usr/bin/env python3
from . import engine


def play():
    name = engine.welcome_user()
    print('What is the result of the expression?')
    right_answer = 0
    while right_answer < engine.NUMBER_ROUNDS:
        result_answer = engine.qestions_game_calc()
        if result_answer:
            engine.correct()
            right_answer += 1
        else:
            engine.not_correct(name)
            break
    if right_answer == 3:
        engine.congrat(name)
