import prompt
from random import randit


def main():
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!\nAnswer 'yes' if the number is even, otherwise answer 'no'")
    index = 0
    winscore = 3
    while index < winscore:
        index += 1
        random_number = randint(1, 100)
        print(f"Question: {random_number}")
        user_name = prompt.string("Your answer: "
        if (user_answer == 'yes' and random_number % 2 == 0) or (user_answer == 'no' and random_number % 2 != 0):
            print 'Correct!'
        elif user_name == "'yes' and random_number % 2 != 0:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!")
        elif user_name == "'no' and random_number % 2 = 0:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {user_name}!")