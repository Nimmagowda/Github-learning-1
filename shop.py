class Shop:#creating class with name of shop
    def __init__(self):
        pass
    
    def item_details(self):
        products = {
            "apereals": {
                "shirt":500,#this is aperals of shop you can by from this 
                "pant": 800,
                "shoes": 1000,
                "spects": 1299,
            },

            "grocry" : {
                "dry_fruits": [599,20],
                "vegetables": 299,
                "cholates": [300,40]
            },

            "sports" : {
                "bats": [2000,10],
                "balls": [500,20],
                "stumps":[3000,4]
            },

        }
        print(products)
        return products

    def add_cart(self):
        self.item_details()
        for i in range(1,5-1):
            select =input("select your items : ")
            self.cart ={}
        
            for category,products in self.item_details().items():
                if select in products:
                    self.cart[select] = products[select]
                    print("==Added your items to cart sucessfuly== : ")
                    break

            else:
                print("product not found : ")

        #print(self.cart)
                
        return self.cart
    #def total_payment(self):
        #print(self.cart{})

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
        print(c1.total_payment())
    elif choice == 5:
            print("exiting")
            break