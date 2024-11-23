import random
print("welcome to hangman!")

words = ["book","banana","apple","fish", "lion","sky","table","tree","flower","fox","python"]

word = random.choice(words)

word_as_list = ["_" for _ in range(len(word))]
tries = 6

while True :
    for letter in word_as_list:
        print(letter , end =" ")

    if "_" not in word_as_list:
        print("congratulations!You win!")
        break

   
    letter = input("\nguess a letter")

    if letter in word:
        print("✅")
        for i in range(len(word_as_list)):
            if letter == word[i]:
             word_as_list[i] = letter

    else:
         print("❌")
         tries -= 1
    
    if tries == 0:
        print("you lose !")
        break
    
print("the End")
