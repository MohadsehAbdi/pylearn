while True:

    username = input()
    password = input()

    if username == "sajjad" and password == "006600":
        print("you have successfully logged in! ✅")
        break
    elif username !="sajjad":
        print("username is incorrect! ❌")
    elif password != "006600":
        print("password is incorrect! ❌")
    else:
        print("something went wrong!")
        
