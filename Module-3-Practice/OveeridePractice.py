class Parent:
    def myMethod(self):
        print("From parent")
class Child(Parent):
    def myMethod(self):
        print("From Child")
        # super(Child, self).myMethod()

ob1=Child()
ob1.myMethod()

