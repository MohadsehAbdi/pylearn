while True:
    print("کاربر عزیز لطفا یک عدد منفی وارد کنید")
    x = int(input())
    if x < 0:
        print("دمت گرم")
        break
    else:
        print("خطا")