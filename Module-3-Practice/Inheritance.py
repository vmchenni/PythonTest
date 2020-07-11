# class base1:
#     def fun(self):
#         print("From Base Class")
#
# class sub(base1):
#     pass
# ob1 = sub()
# ob1.fun()

#  Multiple inheritance


class First:
    def __init__(self):
        super(First, self).__init__()
        print("First")



class Second:
    def __init__(self):
        # super(Second, self).__init__()
        super().__init__()
        print("Second")

class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("From Third")


Third()
print(Third.__mro__)
