class Error(Exception):
    pass


class ValueSmallError(Error):
    pass


class ValueLargeError(Error):
    pass


num = 10
while True:
    try:
        mynum = int(input("Enter number:-"))
        if mynum < num:
            raise ValueSmallError
        elif mynum > num:
            raise ValueLargeError
        else:
            break

    except ValueSmallError:
        print("Its a small value")
    except ValueLargeError:
        print("Its a large value")
print("YOu guessed it right")
