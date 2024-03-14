#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return (name)


def qestions():
    number = randint(1, 100)
    answer = prompt.string('Question: ' + str(number) + ' ')
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    print('Your answer: ' + answer)
    if (answer == correct_answer):
        return True
    print("'yes' is wrong answer ;(. Correct answer was '"
          + correct_answer + "'.")
    return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer = 0
    while right_answer < 3:
        result_answer = qestions()
        if result_answer:
            print('Correct!')
            right_answer += 1
        else:
            print("Let's try again, " + name + "!")
            break
    if right_answer == 3:
        print('Congratulations, ' + name + '!')


if __name__ == '__main__':
    main()
