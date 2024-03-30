from random import randint

# Приветствие
RULE_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Задать вопрос для игры prime
# Возвращает результат ответа
def get_qestion():
    number = randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return [str(number), correct_answer]


# Проверяет является ли число простым
# если число простое то возвращается True
# если нет, то False
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
