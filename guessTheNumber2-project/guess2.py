import random
number = random.randint(1,1000000)
print("lets see if you can guess the number")
while True:
    print("What is your guess")
    guess = int(input("select a number between 1 and 1 000 000: "))
    if guess < number:
        print("too low!")
    elif guess > number:
        print("too high!")
    elif guess == number:
        print("YOU GUESSI IT! CONGRATULATIONS!")
        break
    else:
        print("na na, be always positiv Bro!")
        exit()