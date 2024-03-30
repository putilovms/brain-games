import prompt


# Количество раундов для победы
NUMBER_ROUNDS = 3


def play(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game.RULE_GAME)
    right_answer_counter = 0
    while right_answer_counter < NUMBER_ROUNDS:
        question, right_answer = game.get_qestion()
        answer = prompt.string('Question: ' + question + ' ')
        print('Your answer: ' + answer)
        if right_answer == answer:
            print('Correct!')
            right_answer_counter += 1
        else:
            print("'" + answer + "' is wrong answer ;(. Correct answer was '"
                  + right_answer + "'.")
            print("Let's try again, " + name + "!")
            break
    print('Congratulations, ' + name + '!')
