class Calculator:
    def calci_options(self):
        print("=====select options=====")
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.exit")

    def add(self,a,b):
        return a + b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a * b
    
    def div(self,a,b):
        if a == 0 or b == 0 :
            print("0 is not divisiable")
        else:
            return a / b

c1 = Calculator()



while True:
    c1.calci_options()
    choice = int(input("enter your choice"))

    if choice == 5:
        print("exited")
        break

    elif choice in (1,2,3,4):
        a = int(input("enter a number"))
        b = int(input("enter b number"))
        
    if choice == 1:
        print(c1.add(a,b))

    elif choice == 2:
        print(c1.sub(a,b))
    elif choice == 3:
        print(c1.mul(a,b))
    elif choice == 4:
        print(c1.div(a,b))

    else:
        print("invalid choice")
    

