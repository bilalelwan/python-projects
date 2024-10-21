number = 10
while True:
    print("lets see if you can guess the number")
    guess = int(input("select a number between 1 and 20: "))
    if guess < 5:
        print("too low!")
    elif guess > 15:
        print("too high!")
    elif 5 <= guess < 10 or 10 < guess <= 15:
        print("you are getting close")
    elif guess == 10:
        print("YOU GUESSI IT! CONGRATULATIONS!")
        break
    else:
        print("na na, be always positiv Bro!")
        exit()