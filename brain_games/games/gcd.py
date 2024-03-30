from random import randint

# Приветствие
RULE_GAME = 'Find the greatest common divisor of given numbers.'


# Задать вопрос для игры НОД (GCD)
# Возвращает результат ответа
def get_qestion():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    correct_answer = getGcd(number1, number2)
    qestion = str(number1) + ' ' + str(number2)
    return [qestion, str(correct_answer)]


# Поиск максимального делителя двух чисел
# по алгоритму Евклида
def getGcd(a, b):
    while (a != 0) and (b != 0):
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a + b)


'''
# Список натуральных делителей числа
def getDivs(a):
    divs = []
    for i in range(a):
        if a % (i + 1) == 0:
            divs.append(i + 1)
    return divs


# Поиск максимального делителя двух чисел
def getGcd(a, b):
    divs_a = getDivs(a)
    divs_b = getDivs(b)
    for i in reversed(divs_a):
        if i in divs_b:
            return i

'''
