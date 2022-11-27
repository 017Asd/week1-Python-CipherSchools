winning_number=25
enter_number=int(input("Guess any number from1 to 100: "))
if enter_number==winning_number:
    print("Yow won!")
else:
    if enter_number<winning_number:
        print("Too low")
    else:
        print("Too high")        

