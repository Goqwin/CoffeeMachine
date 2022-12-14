# Godwin JB Mercado 

# Making Drinks (Classes)
# The Coffee Machine serves 3 types of drinks: Tea, coffee, chocolate

# Use cases (Match-cases)
# The drink maker should recieve the correct instructions to the drink
class Drinkmaker:
    def __init__(self):
        self.protocol = {
            "tea": "T:{sugar}:{stick}",       # Used a dictionary to create a format protocol
            "coffee": "C:{sugar}:{stick}",
            "chocolate": "H:{sugar}:{stick}"
        }

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

                
    def send_message(self, message):
        return "M:{message}".format(message=message)

 

    
    

    


