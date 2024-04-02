from random import randint

RULE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_qestion():
    '''Возвращает вопрос и ответ для игры Prime'''
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return [str(number), correct_answer]


def is_prime(number):
    """Если число простое возвращает True, если нет, то False"""
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
