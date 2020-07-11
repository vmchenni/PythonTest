# Design a software for bank system. There should be options like
# cash withdraw, cash credit and change password.
# According to user input, the software should provide required output.

while(1):
    userOption = int((input("Please provide an in put "
                        "1 for cash withdraw, "
                        "2 for cash credit and "
                        "3 for change password.  or "
                        "4 to exit:-")))
    if userOption == 1:
        print("YOu have opted for cash withdraw")
    elif userOption == 2:
        print("YOu have opted for credit card")
    elif userOption == 3:
        print("You have opted for change password")
    elif userOption == 4:
        print("You have opted for exit")
        break
    else:
        print("Incurrect input, Please retry")