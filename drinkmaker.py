# Godwin JB Mercado 

# Making Drinks (Classes)
# The Coffee Machine serves 3 types of drinks: Tea, coffee, chocolate

# Use cases (Match-cases)
# The drink maker should recieve the correct instructions to the drink
class Drinkmaker:
    nbr_of_drinks = 0
    def __init__(self):
        self.protocol = {
            "tea": "T:{sugar}:{stick}",       # Used a dictionary to create a format protocol
            "coffee": "C:{sugar}:{stick}",
            "chocolate": "H:{sugar}:{stick}"
        }
        Drinkmaker.nbr_of_drinks += 1

    def make_drink(self, type:str, sugar, stick): # Make a drink method to take in the orders
        if sugar > 0:
            sugar = int(sugar)
            stick = "0"
        else: 
            sugar = str("")
            stick = ""
        if type == "tea":
                order = self.protocol[type].format(sugar=sugar, stick=stick)
                return order
        elif type == "coffee":
                order = self.protocol[type].format(sugar=sugar, stick=stick)
                return order
        elif type == "chocolate":
                order = self.protocol[type].format(sugar=sugar, stick=stick)
                return order
        else:
            return "Invalid drink type"
    
    def chargedrink(self, type:str):
        totalcost = 0
        while type == "tea" or type == "coffee" or type =="chocolate":
            if type == "tea":
                chargerate = 0.58
                totalcost += chargerate
            elif type == "coffee":
                chargerate =  0.87
                totalcost += chargerate
            elif type == "chocolate":
                chargerate = 0.72
                totalcost += chargerate
        return totalcost


    def cost_message (self, customerwallet:float ,totalcost:float):
        if customerwallet >= totalcost:
            totalcost = totalcost - customerwallet
            print(totalcost)
        else:
            print("Unfortunately you do not have enough money to afford a drink.")
            remainingcost = customerwallet - totalcost
            print("The remaining cost is:", remainingcost)
        

    def send_message(self, message):
        return "M:{message}".format(message=message)

 

    
    

    


