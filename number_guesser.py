import random

top_of_range = int(input("Enter a number greater than 0: "))

if top_of_range < 0:
    print("Enter number greater than 0")
    quit()

random_number = random.randint(0, top_of_range)

guesses = 0
while True:
    guesses+=1
    user_guess = int(input("Guess the number: "))

    
    if user_guess == random_number:
        print("You guessed it right")
        break
    elif user_guess < random_number:
        print("Your guess is less than generated number")
    else:
        print("Your guess is greater than generated number")

print("You guessed the number in", guesses, "guesses.")

