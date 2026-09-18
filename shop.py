#import numpy as np
class Shop:#creating class with name of shop
    def __init__(self):
        self.cart = {}

    
    def item_details(self):
        products = {
            "apereals": {
                "shirt":500,#this is aperals of shop you can by from this 
                "pant": 800,
                "shoes": 1000,
                "spects": 1299,
            },

            "grocry" : {
                "dry_fruits": 599,
                "vegetables": 299,
                "cholates": 300,
            },

            "sports" : {
                "bats": 2000,
                "balls": 500,
                "stumps":3000,
            },

        }
        print(products)
        print("========================================================================")
        return products

    def add_cart(self):
        self.item_details()
        while True:
            select =input("select your items(or type done) : ")
            if select == "done":
                 break
            for category,products in self.item_details().items():
                if select in products:
                    self.cart[select] = products[select]
                    print("==Added your items to cart sucessfuly== : ")
                    #print(self.cart)
                    break    
            else:
                print("product not found : ")   
        print("========================================================================")      
        return self.cart
    def total_items(self):
        print(self.cart)
        self.amount = sum(self.cart.values())
        print("Total amount",self.amount)
        print("========================================================================")
        print("1 : Phone pay")
        print("2 : Google pay")
        print("3 : cash")
        choice = int(input("Enter your Payment Method :  "))
        if choice == 1:
            print("Go Through with Phone pay")
        elif choice == 2:
                    print("Go Through with Google pay")
        elif choice == 3:
                    print("Go Through with Cash")
        else:
            print(f"{choice}this type payment not allowed")


        
c1=Shop()

while True:
    print("1 : iems details : ")
    print("2 : adding to cart : ")
    print("3 : total_items")
    print("5 : exit : ")
    choice =int(input("enter your choice : "))

    if choice == 1:
        c1.item_details()
    elif choice == 2:
        print(c1.add_cart())
    elif choice == 3:
        print("========================================================================")
        print(c1.total_items())
        
    elif choice == 5:
            print("exiting")
            print("Thanks for Visiting")
            break
    else:
         print("invalid choice")