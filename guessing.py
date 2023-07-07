# Write a guessing game program

import random


def get_num_from_player() -> int:
    number_to_guess = -1
    while True:
        try:
            number_to_guess = int(input("Enter a number between 0 and 100: "))
            if number_to_guess <= 0 or number_to_guess >= 100:
                print("Try again")
                continue
        except ValueError:
            print("Enter a number")
            continue

        break
    return number_to_guess


def get_continue_from_player() -> bool:
    player_will_continue = False
    try:
        player_input = input("Continue playing? (y / n): ")
        if player_input == "y" or player_input == "yes" or player_input == "Y":
            player_will_continue = True
    except ValueError:
        pass

    return player_will_continue


if __name__ == '__main__':
    while True:
        num_to_guess = random.randrange(0, 100)
        user_guess = get_num_from_player()

        if num_to_guess == user_guess:
            print("You guessed the number!")
        else:
            print("Incorrect")
        
        if get_continue_from_player():
            continue
        else:
            break
