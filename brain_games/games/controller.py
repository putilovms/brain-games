#!/usr/bin/env python3
from . import engine


def play(game):
    name = engine.welcome_user()
    print_rule_game(game)
    right_answer = 0
    while right_answer < engine.NUMBER_ROUNDS:
        result_answer = qestions_game(game)
        if result_answer:
            engine.correct()
            right_answer += 1
        else:
            engine.not_correct(name)
            break
    if right_answer == 3:
        engine.congrat(name)


def print_rule_game(game):
    match game:
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'calc':
            print('What is the result of the expression?')
        case 'gcd':
            print('Find the greatest common divisor of given numbers.')
        case 'progression':
            print('What number is missing in the progression?')
        case 'prime':
            print('Answer "yes" if given number is prime.' +
                  + 'Otherwise answer "no".')


def qestions_game(game):
    match game:
        case 'even':
            return engine.qestions_game_even()
        case 'calc':
            return engine.qestions_game_calc()
        case 'gcd':
            return engine.qestions_game_gcd()
        case 'progression':
            return engine.qestions_game_progression()
        case 'prime':
            return engine.qestions_game_prime()
