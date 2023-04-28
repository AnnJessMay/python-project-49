import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION_GAME)
    counter = 0
    number_of_attempts = 3
    while counter < number_of_attempts:
        question, correct = game.generated_question_and_answer()
        print(f'Question: {question}')
        prompt_answer = input("Your answer: ")
        if correct == prompt_answer:
            counter += 1
            print('Correct!')
        else:
            print(f'''"{prompt_answer}" is wrong answer ;(.
Correct answer was "{correct}".
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')
