import random

secret_number = random.randint(0,100)
count = 0
while True:
    guess_number = int(input("please enter a number"))
    count = count + 1
    if guess_number == secret_number:
        print("congratulation!🎉")
        print("you guessed the secret number in", count, "attempts")
        break

    elif guess_number<secret_number:
        print("too low!try again")

    elif guess_number>secret_number:
        print("too hight! try again")

