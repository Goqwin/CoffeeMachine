import drinkmaker as dm

drinks = ["tea", "coffee", "chocolate"] 


def main():
    print("Welcome to Goqwin's Drink Maker #1") # This is based off a CM in github (Iteration #1)
    order()


def order():
    drinkorder = input("Enter the type of drink you'd like: ").lower()
    sugaramount = int(input("How much sugar would you like: "))
    dm_instance = dm.Drinkmaker()
    stick = ""
    drinkorder = dm_instance.make_drink(drinkorder, sugaramount, stick)
    print(drinkorder)

if __name__ == "__main__":
    main()