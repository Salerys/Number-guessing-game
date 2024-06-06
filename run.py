import random


def get_username():
    #   Ask and validate the user's name
    print("Welcome to the number guessing game!", end="")
    username = input("How can I call you?\n")

    while not username.isalpha():
        print("Your name can only contain letters.", end="")
        username = input("Please tell me your name correctly!\n")

    if username.isalpha():
        return username


#   Main function
def number_guessing_game():

    #   Generate a random number
    generated_number = random.randint(1, 100)

    #   Get the user's name and count the number of guesses
    username = get_username()
    number_of_guesses = 0

    print(f"{username.capitalize()} guess your number between 1 and 100.")

    while True:
        guess = input("Enter your number: ")

        #   Check if the guess is a valid number
        if validate_number(guess):
            continue

        #   Convert guess into integer if it is a valid number
        guess = int(guess)

        #   Check if the guess is within the range
        if check_number_range(guess):
            continue

        #   Increment the guesses
        number_of_guesses += 1

        #   Check if the guess is correct, if yes then exit the game
        if compare_numbers(generated_number, guess):
            print(
                f"Congratulations {username}! You've guessed the number \
                {generated_number} correctly in {number_of_guesses} guess(es)."
            )
            break


#   Check if the guess is a valid number and not a letter or symbol
def validate_number(number):
    try:
        int(number)
    except ValueError:
        print("Please enter a valid number")
        return True


#   Check if the guess is within the range
def check_number_range(number):
    if number < 1 or number > 100:
        print("Please enter a number within the range of 1 and 100")
        return True


#   Check if the guessed number is lower/higher than the generated number
#   or the same
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
