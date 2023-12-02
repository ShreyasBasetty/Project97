import random

number=random.randint(1,100)
chances=0
print("Guess a number (between 1 to 100):")

while chances < 5:
    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("CONGRATULATIONS YOU HAVE GUESSED IT RIGHT")
        break

    elif guess < number:
        print("Guessed Number Is Small, Try a Bigger Number")

    else:
        print("The Number Guessed is Bigger, Try a Smaller Number ")

    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is", number)