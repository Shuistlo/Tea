"""
Maybe i'll make a tea class
"""

class Tea:
        """
        possible intializer
        """
        def __init__(self, teaBase, size = 12, toppings = None, milk = False, sugarAmount = 0, temperature = None):
                """
                the full set
                size = float (default to 12 ounces)
                toppings = []
                teaBase = string
                milk = boolean
                sugarAmount = double
                temperature = string (hot cold warm)
                """
                temperatureList = ["hot", "cold", "warm"]
                toppingsList = ["pearls", "lychee jelly", "coconut jelly", "oats", "red beans", "aiyu jelly"] #sure there's more

                #need something for the teaBase still
                if type(size) != None and type(size) != float:
                    raise TypeError()
                if toppings != None:
                    for item in toppings:
                        if item not in toppingsList:
                            raise ValueError()
                if temperature == None:
                    temperature = "hot"
                if temperature not in temperatureList:
                    raise ValueError()

                if milk != None and type(milk) != boolean:
                    raise TypeError()
                if type(sugarAmount) != float:
                    raise TypeError()
                
                self.size = size
                self.toppings = toppings
                self.teaBase = teaBase
                self.milk = milk
                self.sugarAmount = sugarAmount
                self.temperature = temperature
                
        def getSize(self):
                """
                gets size
                """
                return self.size

        #other getters 
        
        def __str__(self):
                """
                returns a string interpretation of the tea
                """
                strTea = "A lovely " + self.size + " ounce cup of tea, made with " + self.teaBase + "."
                if (self.milk == False) and (toppings == None):
                    return strTea
                strTea2 = "Contains milk, "
                if self.milk == False:
                    strTea2 = " Contains "
                for item in toppings:
                    strTea2 + item + " "
                strTea2 = strTea2[:-1] + "." 
                return strTea + strTea2

#c = Tea("oolong", 12, ["pearls", "coconut jelly"], False, 23.4, "hot")
d = Tea("oolong")
print(d)
try:
    a = Tea("oolong", "green")
    print(a)
except ValueError:
    print("value error")
#except TypeError
