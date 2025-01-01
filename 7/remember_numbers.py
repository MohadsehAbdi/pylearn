import random
import time
import os


print("welcome to the remember number game")
print("try to remember the sequence of number and repeat it")
print("the sequence will get longer each round, let's see how far yo can go")
print("type'quit' anytime to stop playing")

sequence = []
round_number = 1

while True:
    print("round", round_number)

    new_number=random.randint(0, 9)
    sequence.append(new_number)

    print("remember this sequence:")
    print(sequence)

    time.sleep(5)

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print("now enter the sequence number by number:")
    player_sequence = []
    for i in range(len(sequence)):
        user_input = input()


        if user_input == "quit":
            print("Thanks for playing!see you next time")
            exit()
        else:
            player_sequence.append(int(user_input))

    if player_sequence == sequence:
        print("correct!")
        round_number += 1
    else:
        print("Oops! that was incorrect")
        print(f"you made it round {round_number}, Good job")
        break