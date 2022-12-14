import drinkmaker as dm

drinks = ["tea","coffee", "chocolate"] 


def main():
    print("Welcome to Goqwin's Drink Maker #1") # This is based off a CM in github (Iteration #1)
    order()


def order():
    drinkorder = input("Enter the type of drink you'd like: ").lower()
    while drinkorder != "":
        sugaramount = int(input("How much sugar would you like: "))
        dm_instance = dm.Drinkmaker()
        stick = ""
        drinkorder = dm_instance.make_drink(drinkorder, sugaramount, stick)
        charge(drinkorder)
        print(drinkorder)
        drinkorder = input("Enter the type of drink you'd like: ").lower()
       
    

def charge(drinkorder):
    dm_instance = dm.Drinkmaker()    
    totalcost = dm_instance.chargedrink(drinkorder)
    print("The total cost is:", totalcost)

if __name__ == "__main__":
    main()