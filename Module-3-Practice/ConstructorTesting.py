class myClass:
    def __init__(self):
        print("From Constructor")
    def __del__(self):
        print("From Desctructor")
ob1=myClass()
# ob1.__del__()
if __name__=="_main__":
    del  ob1