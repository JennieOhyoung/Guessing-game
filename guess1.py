# Write a program named guess.py that plays the 'number guessing game'.
# The computer will choose a random number between 1 and 100, 
# and ask the user to guess the number
# giving them a hint if it's high or low

from random import randint 
random_number = randint(1, 100)

#Greeting

name = raw_input("Hello, whats your name? ")
print "Well, %s, I'm thinking of a number between 1 and 100." % name
print "Think you can guess what it is?"

guessing = True

number_of_tries = 0


while (guessing):
    guess = raw_input("What's your guess? ")
    if type(guess) != int:
    
        print "That's not a number! Guess again!"
    else:
        int(guess)
        if guess < 1 or guess > 100:
            print "That number is not in range, guess again!"

        elif guess > random_number:
            print "Your guess is too high."
            number_of_tries += 1

        elif guess < random_number:
            print "Your guess is too low."
            number_of_tries += 1

        elif guess == random_number:
            number_of_tries += 1
            print "You've got it %s ! You found my number in %d tries!" % (name, number_of_tries)
            guessing = False

        else:
            guessing = False