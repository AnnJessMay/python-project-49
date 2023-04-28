import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION_GAME)
    counter = 0
    number_of_attempts = 3
    while counter < number_of_attempts:
        generated_question, correct = game.print_question()
        print(f'Question: {generated_question}')
        get = input("Your answer: ")
        if correct == get:
            counter += 1
            print('Correct!')
        else:
            print(
                f'''"{get}" is wrong answer ;(. Correct answer was "{correct}".
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')
