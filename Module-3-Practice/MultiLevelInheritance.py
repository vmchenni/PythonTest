class Animal:
    def eat(self):
        print("Eat")


class Dog(Animal):
    def bark(self):
        print("Bark")


class BabyDog(Dog):
    def weep(self):
        print("Weep")


d = BabyDog();

print(BabyDog.__mro__)
d.eat()
d.bark()
d.weep()
