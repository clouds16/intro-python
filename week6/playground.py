class Fruits:
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.quantity = 0
        self.color = "none"

    def updatePrice(self, price):
        self.price = price
        return self.price

    def updateQuantity(self, quantity):
        self.quantity = quantity
        return self.quantity

    def updateColor(self, color):
        self.color = color
        return self.color


def main():
    fruits = ["Apple", "Banana", "Pear"]

    for items in fruits:
        itemDict = {}

        currentItem = Fruits(items)

        itemDict[items] = Fruits(items)

    print(itemDict)


main()
