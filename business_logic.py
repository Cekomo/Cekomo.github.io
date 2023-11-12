
class BusinessLogic():
    def __init__(self):
        self.option_holder = ["Ryzen 7 7700X", "Corsair Vengeance", 
                              "ASUS X670", "Samsung EVO 970", "Quitted"]
        
    def print_from_opt(self, navigation):
        print(self.option_holder[navigation])

    