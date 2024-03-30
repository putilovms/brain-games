from random import randint


RULE_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_qestion():
    number = randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return [str(number), correct_answer]
