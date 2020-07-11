# class Edureka():
#     def __init__(self):
#         self.__pri="I am Private"
#         self._pro="I am Protected"
#         self.pub="I am public"
#         # print()
#
# ob=Edureka();
# print(ob.pub)
# print(ob._pro)
# print(ob.__pri)

class MyClass():
    def mypublicmethod(self):
        print("Public Method")
    def __privateMethod(self):
        print("From Private Method")

# myclass=MyClass()
# myclass.mypublicmethod()
# # myclass.__privateMethod()
# myclass._MyClass__privateMethod()

class Edureka:
    domain=("Data science")
    def setCource(self,name,*Names):
        self.name=name
        print(self.name)
        for var in Names:
            print(var)

ob1=Edureka()
ob2=Edureka()

ob1.setCource("Python")
ob2.setCource("Machine Learning", "Testing", "Automation")

print(ob1.domain)
ob1.domain="GOD"

print(ob1.domain)
print(ob2.domain)

print(ob1.name)
print(ob2.name)