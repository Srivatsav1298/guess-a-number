import random
guessesTaken = 0
secretNumber = random.randint(1,20)
print("Let's play agame, I am thinking of a number between 1and 20")
#Ask the player to guess 7 times
while guessesTaken < 8:
    print("Please take a guess!")
    guess=int(input())

    guessesTaken +=1

    if guess < secretNumber:
        print("Your Guess is too low!")
    elif guess > secretNumber:
        print("Your guess is too high!")
    else:
        break #This condition is the correct guess
if guess == secretNumber:
    print("Awesome! you have guessed my number in " + str(guessesTaken) + " guesses")
else:
    print("Nope.Game is over. The number I was thinking of was " +str(secretNumber))
