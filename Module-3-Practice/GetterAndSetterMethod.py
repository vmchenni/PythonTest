class Edureka:
    def __init__(self, courseName):
        self.courseName = courseName

    def setCourseName(self, courseName):
        self.courseName = courseName

    def getCourseName(self):
        # print(self.courseName)
        return self.courseName


ob = Edureka("Python")
print(ob.getCourseName())

ob.setCourseName("machine Learning")
print(ob.getCourseName())
