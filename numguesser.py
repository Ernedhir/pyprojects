import random

print("Welcome to the Number Guesser! In this game, you will select a range (Starting from 1) of numbers to select. \nAfter that, you will try to find that number between the range you specified.")
rng = int(input("Range: "))

numb = random.randint(1, rng)

print(numb)

guess = int(input("Your guess: "))
if guess == numb: print("WOW! You guessed it within first try.")
else:
    guesses=1
    while True:
        if guess > numb:
            guess = int(input(f"Lower than {guess}!\n"))
            guesses+=1
        elif guess < numb:
            guess = int(input(f"Higher than {guess}!\n"))
            guesses+=1
        elif guess == numb: 
            print(f"Congratz! You guessed it in {guesses} try!")
            break

