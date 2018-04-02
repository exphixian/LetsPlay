import random

guesses = 0
number = random.randint(1,50)
print("I am thinking of a number between 1 and 50.  Take a guess!")

for guesses in range(6):
    guess = int(input())

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    elif guess == number:
        print("That's right!")
        break

if guess == number:
    guesses += 1
    print("You guessed it right in %s guesses!" % (guesses))
else:
    print("Sorry, but the number was %s" % (number))
