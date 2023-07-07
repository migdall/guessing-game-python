# Write a guessing game program

import random


def get_num_from_player() -> int:
    number_to_guess = -1
    while True:
        try:
            number_to_guess = int(input("User 1, enter a number between 0 and 100: "))
            if number_to_guess <= 0 or number_to_guess >= 100:
                print("Try again")
                continue
        except ValueError:
            print("Enter a number")
            continue

        break
    return number_to_guess

if __name__ == '__main__':
    num_to_guess = random.randrange(0, 100)
    user_guess = get_num_from_player()

    if num_to_guess == user_guess:
        print("You guessed the number!")
    else:
        print("Incorrect")
