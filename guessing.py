# Write a guessing game program

number_to_guess = -1
user_two_guess = -1

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


while True:
    try:
        user_two_guess = int(input("User 2, guess the number: "))
        if user_two_guess <= 0 or user_two_guess >= 100:
            print("Try again")
            continue
    except ValueError:
        print("Enter a number")
        continue

    break

if number_to_guess == user_two_guess:
    print("You guessed the number!")
else:
    print("Incorrect")
