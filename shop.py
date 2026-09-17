#import numpy as np
class Shop:#creating class with name of shop
    def __init__(self):
        self.cart = {}
        self.t_amount = t_amount

    
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
        return products

    def add_cart(self):
        self.item_details()
        for i in range(1,3):
            select =input("select your items : ")
        
            for category,products in self.item_details().items():
                if select in products:
                    self.cart[select] = products[select]
                    print("==Added your items to cart sucessfuly== : ")
                    #print(self.cart)
                    break    
            else:
                print("product not found : ")         
        return self.cart
    def total_items(self):
        print(self.cart)
        """amount =np.array[self.cart.values()]
        print(np.amount)
        self.t_amount = 0
        for a in self.cart.values():
            self.t_amount += a
            break
        print(self.t_amount)
        return self.t_amount"""

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
        print(c1.total_items())
        a = o
        
    elif choice == 5:
            print("exiting")
            break