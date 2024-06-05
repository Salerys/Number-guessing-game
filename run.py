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

    print(f"{username.capitalize()} guess your number between 1 and 100.")

    while True:
        guess = input("Enter your number: ")

        if validate_number(guess):
            continue

        guess=int(guess)

        if check_number_range(guess):
            continue

        print(f"Your number is: {guess}")
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

number_guessing_game()