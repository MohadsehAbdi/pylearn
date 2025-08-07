def  read_from_file():
    global words_bank

    f = open( "s8/Translate.txt", "r")

    temp = f.read().split("\n")
    f.close()
    words_bank = []
    for i in range (0, len(temp), 2):
        my_dict = {"en": temp[i], "fa": temp[i+1]}
        words_bank.append(my_dict)



    
def translate_english_to_persian():
    
    user_text = input("enter your english text:")
    user_words = user_text.split(" ")
    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output = output + word["fa"] + " "
                break
        else:
            output = output + user_word + " "

    print(output)
def trenslate_persian_to_english():
     
    user_text  = input("inter your persian text:") 
    user_words = user_text.split(" ")
   
    output = ""
    
    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                output = output + word["en"] + " "
                break
        else:
            output = output + user_word + " "

    print(output)

def add_new_word_to_detabase():

    english_word = input("write english  word")
    persian_word = input("write persian word")
    with open("Translate.txt" ,  "a") as f:
        f.write(f"{persian_word}\n{english_word} \n")
    words_bank.append({"en":english_word, "fa": persian_word})
    print("thank you for new word 💖")
 


def show_menu():
    print("welcome to my translate")
    print("1_Translate english to persian:")
    print("2_Translate persian to english:")
    print("3_addnew word to detabase:")
    print("4_exit")




words_bank = []
read_from_file()
while True:

    show_menu()
    choice = int(input("inter your choice:"))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        trenslate_persian_to_english()
    elif choice == 3:
        add_new_word_to_detabase()
    elif choice == 4:
        exit(0)



