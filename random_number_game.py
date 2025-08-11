from random import randint


def play_guessing_game():
    secret_number = randint(0, 100)
    while True:
        user_guess = input("Guess a number between 0 and 100: ")
        if user_guess.isdigit() and int(user_guess) <= 100:
            user_guess_tr = int(user_guess)
            if user_guess_tr == secret_number:
                return f"Slay girllll, you guessed the number {secret_number}!!!"
            elif user_guess_tr > secret_number:
                print("Too high!")
            else:
                print("Too low!")

        else:
            print("Please enter a valid number between 0 and 100")


print(play_guessing_game())
