import random

RULE_GAME = 'What is the result of the expression?'


def get_qestion():
    """Возвращает вопрос и ответ для игры Calc"""
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    operation = random.choice(["+", "-", "*"])
    correct_answer = math_operation(number1, number2, operation)
    qestion = str(number1) + ' ' + operation + ' ' + str(number2)
    return [qestion, str(correct_answer)]


def math_operation(number1, number2, operation):
    """ Возвращает результат математической операции"""
    result = 0
    match operation:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
    return result
