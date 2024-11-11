import random

computer_number = random.randint(0 , 100)
while True:
    user_number = int(input())

    if user_number == computer_number:
        print("افرین! 🎉🎉🎉🎉")
        break
    elif user_number < computer_number:
        print("برو بالا تر")
    else:
        print("برو پایین تر")
