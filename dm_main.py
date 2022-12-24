import drinkmaker as dm

drinks = ["tea","coffee", "chocolate"] 


def main():
    print("Welcome to Goqwin's Drink Maker #1") # This is based off a CM in github (Iteration #1)
    customer_wallet = float(input("Enter your wallet balance: "))
    order(customer_wallet)


def order(customer_wallet):
    while True:
        drinkorder = input("Enter the type of drink you'd like: ").lower()
        if drinkorder == "":
            break
        elif drinkorder == "exit":
            break
        else:
            sugaramount = int(input("How much sugar would you like: "))
            dm_instance = dm.Drinkmaker()
            stick = ""
            if dm_instance.check_payment(dm_instance.chargedrink(drinkorder), customer_wallet):
                drinkorder = dm_instance.make_drink(drinkorder,sugaramount,stick)
                charge(drinkorder, customer_wallet)
                drinkorder = input("Enter the type of drink you'd like: ").lower()
            else:
                print("Your drink order has been cancelled.")
    print(drinkorder)


       
    

def charge(drinkorder,customer_wallet):
    dm_instance = dm.Drinkmaker()    
    totalcost = dm_instance.chargedrink(drinkorder)
    customer_wallet -= totalcost
    print("The total cost is:", customer_wallet)
if __name__ == "__main__":
    main()