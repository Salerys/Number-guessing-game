def get_username():
    #   Ask and validate the user's name
    username = input("Welcome to the number guessing game! How can I call you?\n")

    while not username.isalpha():
        username = input(
            "Your name can only contain letters. Please tell me your name correctly!\n"
        )

    if username.isalpha():
        return(username)

get_username()

