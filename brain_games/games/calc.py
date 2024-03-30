from random import randint


# Приветствие
RULE_GAME = 'What is the result of the expression?'


# Задать вопрос для игры Even
# Возвращает результат ответа
def get_qestion():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    math_op = randint(1, 3)
    correct_answer, operation = math_operation(number1, number2, math_op)
    qestion = str(number1) + ' ' + operation + ' ' + str(number2)
    return [qestion, str(correct_answer)]


# Возвращает список с результатом математической операции
# и символ математической операции
def math_operation(number1, number2, math_op):
    result = []
    match math_op:
        case 1:
            result.append(number1 + number2)
            result.append('+')
        case 2:
            result.append(number1 - number2)
            result.append('-')
        case 3:
            result.append(number1 * number2)
            result.append('*')
    return (result)
