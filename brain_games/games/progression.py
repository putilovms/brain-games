from random import randint

# Приветствие
RULE_GAME = 'What number is missing in the progression?'


# Задать вопрос для игры progression
# Возвращает результат ответа
def get_qestion():
    PROG_LEN = 10
    prog = prog_gen(PROG_LEN, randint(1, 10), randint(1, 20))
    hide_number = randint(0, PROG_LEN - 1)
    correct_answer = prog[hide_number]
    prog[hide_number] = '..'
    return [' '.join(map(str, prog)), str(correct_answer)]


# Генерирует арифметическую прогрессию длинной lenght,
# с шагом step, начиная с числа start
def prog_gen(lenght, step, start):
    progression = [(i * step) + start for i in range(lenght)]
    return (progression)
