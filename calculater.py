class Calculator:
    def calci_options(self):
        print("=====select options=====")
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.exit")

    def input(self):
        a = int(input("enter a number"))
        b = int(input("enter b number"))


    def add(self,input):
        print(input())
        #a = int(input("enter a number"))
        #b = int(input("enter b number"))
        return a + b

    def sub(self,input):
        #a = int(input("enter a number"))
        #b = int(input("enter b number"))
        return a - b

    def mul(self,input):
        #a = int(input("enter a number"))
        #b = int(input("enter b number"))
        return a * b
    
    def div(self,input):
        #a = int(input("enter a number"))
        #b = int(input("enter b number"))
        return a / b

c1 = Calculator()
#c1.add()

while True:
    print(c1.calci_options())
    choice = int(input("enter your choice"))
    if choice == 1:
        #print(c1.input())
        print(c1.add())

    elif choice == 2:
        print(c1.sub())
    elif choice == 3:
        print(c1.mul())
    elif choice == 4:
        print(c1.div())
    elif choice == 5:
        print("exited")
        break
    

