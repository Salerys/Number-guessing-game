import random

def get_username():
    #   Ask and validate the user's name
    username = input("Welcome to the number guessing game! How can I call you?\n")

    while not username.isalpha():
        username = input(
            "Your name can only contain letters. Please tell me your name correctly!\n"
        )

    if username.isalpha():
        return(username)

def number_guessing_game():

    generated_number = random.randint(1, 100)

    username = get_username()

    number_of_guesses = 0

    print(f"{username.capitalize()} guess your number between 1 and 100.")

    while True:
        guess = input("Enter your number: ")

        if validate_number(guess):
            continue

        guess=int(guess)

        if check_number_range(guess):
            continue

        number_of_guesses += 1

        if compare_numbers(generated_number, guess):
            print(
                f"Congratulations {username}! You've guessed the number {generated_number} correctly in {number_of_guesses} guess(es)."
            )
            break

def validate_number(number):
    try:
        int(number)
    except ValueError:
        print("Please enter a valid number")
        return True

def check_number_range(number):
    if number < 1 or number > 100:
        print("Please enter a number within the range of 1 and 100")
        return True

def compare_numbers(gen_num, user_num):
    if user_num < gen_num:
        print("Your guess is too low! Try guessing higher.")
        return False
    elif user_num > gen_num:
        print("Your guess is too high! Try guessing lower.")
        return False
    else:
        return True

number_guessing_game()