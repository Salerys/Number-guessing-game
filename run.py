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

    username = get_username()

    print(f"{username.capitalize()} guess your number between 1 and 100.")

    while True:
        guess = input("Enter your number: ")

        if validate_number(guess):
            continue

        print(f"Your number is: {guess}")
        break

