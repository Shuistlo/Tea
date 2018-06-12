"""
Maybe i'll make a tea class
"""


class Tea:
    """
    possible intializer
    """

    def __init__(self, teaBase, size=12.0, toppings=None, milk=False, sugarAmount=0.0, temperature=None):
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
        toppingsList = ["pearls", "lychee jelly", "coconut jelly", "oats", "red beans",
                        "aiyu jelly"]  # sure there's more

        # need something for the teaBase still
        if type(size) != None and type(size) != float:
            raise TypeError("Incorrect type for size")
        if toppings != None:
            for item in toppings:
                if item not in toppingsList:
                    raise ValueError("This is not a topping")
        if temperature == None:
            temperature = "hot"
        if temperature not in temperatureList:
            raise ValueError("This is not a temperature")

        if milk != None and type(milk) != bool:
            raise TypeError("The type for milk is a boolean")
        if type(sugarAmount) != float or not (sugarAmount >= 0 and sugarAmount <= 1):
            raise TypeError("The type for sugar has to be a float between 0 and 1")

        self.size = size
        self.toppings = toppings
        self.teaBase = teaBase
        self.milk = milk
        self.sugarAmount = sugarAmount
        self.temperature = temperature

    def getBase(self):
        return self.teaBase

    def getSize(self):
        return self.size

    def getToppings(self):
        return self.toppings

    def getMilk(self):
        return self.milk

    def getSugar(self):
        return self.sugarAmount

    def getTemp(self):
        return self.temperature

    def setBase(self, base):
        self.teaBase = base

    def setSize(self, nSize):
        self.size = nSize

    def setToppings(self, nToppings):
        return
    # no functionality yet

    def setMilk(self, nMilk):
        self.milk = nMilk

    def setSugar(self, nSugar):
        self.sugarAmount = nSugar

    def setTemp(self, nTemp):
        self.temperature = nTemp

    def __str__(self):
        """
        returns a string interpretation of the tea
        """
        strTea = "A lovely " + str(self.size) + " ounce cup of tea, made with " + self.teaBase + "."
        if (self.milk == False) and (self.toppings == None):
            return strTea
        strTea2 = "Contains milk, "
        if self.milk == False:
            strTea2 = " Contains "
        for item in self.toppings:
            strTea2 + item + " "
        strTea2 = strTea2[:-1] + "."
        return strTea + strTea2


# c = Tea("oolong", 12, ["pearls", "coconut jelly"], False, 23.4, "hot")
d = Tea("oolong")
print(d)
try:
    a = Tea("oolong", 12.0, None, True, 0.0, "almost cold")
    print(a)
except ValueError as e:
    print(e)
# except TypeError
