from random import randint

RULE_GAME = 'Find the greatest common divisor of given numbers.'


def get_qestion():
    '''Возвращает вопрос и ответ для игры Gcd'''
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    correct_answer = getGcd(number1, number2)
    qestion = str(number1) + ' ' + str(number2)
    return [qestion, str(correct_answer)]


def getGcd(a, b):
    '''Возвращает НОД по алгоритму Евклида'''
    while (a != 0) and (b != 0):
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a + b)
