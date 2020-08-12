from mainclass.test import *


class Child(Student):

    def greet(self):
        k = Student()
        print(k.avg())


x = Child()
x.greet()
