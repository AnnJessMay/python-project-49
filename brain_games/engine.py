import prompt

number_of_rounds = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    counter = 0
    while counter < number_of_rounds:
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        prompt_answer = prompt.string("Your answer: ")
        if correct_answer == prompt_answer:
            counter += 1
            print('Correct!')
        else:
            print(f'"{prompt_answer}" is wrong answer ;(.'
            f'Correct answer was "{correct_answer}".'
            f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
