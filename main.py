import random
secret = random.randrange(0,1024)
guess = 0
guess_count = 0
prev_guess = []
min_guess = 10

print("It's a guessing game! The computer has randomly selected a number greater than 0, but less than 1,024. Can you guess what it is?")
while guess != secret:
    try:
        guess = int(input("\nGuess a number!: "))
        if guess in prev_guess: #skips if number has already been guessed
            print("You've already guessed that number! Don't worry, it won't impact your number of tries.")
            pass
        elif guess < 1 or guess > 1023: #in case number is beyond bounds of game
            print("Ooh! Your number is either too small or too large - the computer would never have selected that number. Don't worry, it won't impact your number of tries.")
        else:
            prev_guess.append(guess)
            guess_count += 1
            if guess > secret:
                print("That's too big!", end=" ")
            elif guess < secret:
                print("That's too small!", end=" ")
            if guess != secret: #tells user total number of tries every round
                print("So far you've tried " + str(guess_count), end=" ")
                if guess_count == 1: #corrects for single 'time' versus 'times'
                    print("time.")
                else:
                    print("times.")
    except ValueError: #in case user inputs text or a decimal
        print("Oops, that's an invalid response. Make sure you put in a positive integer (a number without the decimal).")

print("\n\nYou got it!! The number was " + str(secret) + ". You took " + str(guess_count))
if guess_count == 1: #corrects for single 'time' versus 'times'
    print("try", end=" ")
else:
    print("tries", end=" ")
print("to solve it.\n")
if guess_count == 1: #in case, by some stroke of luck, the user wins on the first try
    print("Wait a minute... 1 TRY!?! You must have some serious luck today!!! Quick, enter a lottery!")
else: #finds minimum number of tries needed using 'secret method'. finds lowest multiple of 2 that is a factor of the number, which can indicate the lowest valued bit in the binary form of the number. this can be used to find the minimum number of tries.
    while guess % 2 == 0:
        min_guess -= 1
        guess = guess / 2
    if guess_count > min_guess:
        print("Did you know that there is a way, without blindly guessing, that you can guarantee finding the answer in 10 tries or less? It's true! You could have guessed " + str(secret) + " in " + str(min_guess), end=" ")
        if min_guess == 1: #corrects for single 'time' versus 'times'
            print("try.", end=" ")
        else:
            print("tries.", end=" ")
        print("Can you find the method?")
    elif guess_count < min_guess:
        print("Wow! You needed less guesses than necessary! You must have some good luck. Normally, you would need " + str(min_guess), end=" ")
        if min_guess == 1: #corrects for single 'time' versus 'times'
            print("try", end=" ")
        else:
            print("tries", end=" ")
        print("to guarantee that you will find the answer. Do you know why?")
    else:
        print("Nice job! That is the minimum number of tries you needed to guarantee finding the number! Did you use the secret method?")
    print("Here is a hint: 512")
