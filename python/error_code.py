import os, sys

x = 42


def myFunc(x, y):
    return x + y


def Unused():
    pass


class test:
    def __init__(self, value):
        self.Value = value

    def printvalue(self):
        print("The value is: " + str(self.Value))


def main():
    result = myFunc(x, 5)
    print(result)
    t = test(10)
    t.printvalue()


main()
