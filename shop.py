class Shop:#creating class with name of shop
    def __init__(self):
        pass
    
    def item_details(self):
        items = {
            "apereals": {
                "shirt":{ "price":500,"qt":10},#this is aperals of shop you can by from this 
                "pant": { "price":800,"qt":10},
                "shoes": { "price":1000,"qt":10},
                "spects": { "price":1299,"qt":10},
            },

            "grocry" : {
                "dry_fruits": [599,20],
                "vegetables": 299,
                "cholates": [300,40]
            },

            "sports" : {
                "bats": [2000,10],
                "balls": [500,20],
                "stumps":[3000,4"sects"]
            }
        }
    def add_cart(self):
        cart ={}
        select =input("select your items")
        for select in c1.items :
            cart["select"] = c1.items["select"]
            print("added your items to cart sucessfuly")
c1=Shop()

while True:
    print("1 iems details")
    print("adding to cart")
    choice =int(input("enter your choice"))

    if choice == 5:
        print("exiting")
        break
    elif choice == 1:
        print(c1.item_details())
    elif choice == 2:
        print(c1.add_cart())

    