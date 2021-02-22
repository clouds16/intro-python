import json


class MachineStatus:
    # Claas imports the label for that specific machine
    def __init__(self, label):
        self.label = label
        self.beverages = 0
        self.currentbeverages = 0
        self.totalincome = 0
        self.percentsold = 0
    # return individual variables

    def getLabel(self):
        return self.label

    def getBeverages(self):
        return self.beverages

    def getCurrentBeverages(self):
        return self.currentbeverages

    # Update current values from the data
    def updateLabel(self, machinelabel):
        self.label = machinelabel
        return self.label

    def getTotalIncome(self):
        return self.totalincome

    def updateBeverages(self, newbeverage):
        self.beverages = self.beverages + newbeverage
        return self.beverages

    def updateCurrentBeverages(self, addcurrentb):
        self.currentbeverages = self.currentbeverages + addcurrentb
        return self.currentbeverages

    # dont need this , but easy to update when called, can do so in the variable name as well
    def updateIncome(self, itemprice, currentstock, laststock):
        self.totalincome = self.totalincome + \
            itemprice * (laststock - currentstock)
        # self.percentsold = self.currentbeverages / self.beverages
        return self.totalincome

    def getPercentSold(self):
        return self.percentsold

    # current percentage is full - current
    def updatePercentages(self):
        self.percentsold = (1-(self.currentbeverages/self.beverages))*100
        return self.percentsold

    def printLabel(self):
        print("{}         {:.2f}%    ${:.2f}".format(
            self.label, self.percentsold, self.totalincome))

    # printable representation of class items - when trying to print class instance from the dictionary created
    def __repr__(self):
        return 'Name: {}, Previous Stock: {}, Current Stock: {}, Total Income: {}, Percent Sold: {}'.format(self.label, self.beverages, self.currentbeverages, self.totalincome, self.percentsold)


class InventoryItem:
    def __init__(self, itemName):
        self.name = itemName
        self.totalStocked = 0
        self.totalInStock = 0
        self.totalSlots = 0

    def addToStocked(self, stockAmt):
        self.totalStocked = self.totalStocked + stockAmt

    def addToInStock(self, inStockAmt):
        self.totalInStock = self.totalInStock + inStockAmt

    def incrementSlots(self):
        self.totalSlots = self.totalSlots + 1

    def getNumberSold(self):
        return self.totalStocked - self.totalInStock

    def getSoldPct(self):
        return self.getNumberSold() / self.totalStocked

    def getStockNeed(self):
        return 8 * self.totalSlots - self.totalInStock

    def getName(self):
        return self.name

    def getNumberInStock(self):
        return self.totalInStock

    def __repr__(self):
        return '{} In Stock: {}, Stocked: {}, Slots: {}'.format(self.name, self.totalInStock, self.totalStocked, self.totalSlots)


# New function to choose to either look at machine report or invntory report

def main():

    while True:
        userinput = str(
            input("Would you like the machine report(m) or the inventory report(i) or (q) to quit ?  "))

        if userinput == "m":
            machineReport()
        elif userinput == "i":
            inventoryReport()
        elif userinput == "q":
            exit()
        else:
            print("Try again!")

# new isolated logic for machine report


def machineReport():
    inventoryFileNames = ["REID_1F_20171004.json",
                          "REID_2F_20171004.json", "REID_3F_20171004.json"]
    # create dictionary to hold values
    machineData = {}

    # iterate through files
    print("{}         {}%    ${}".format("Label", "%Sold", "Sales Total"))
    for inventoryFileName in inventoryFileNames:
        inventoryFile = open(inventoryFileName, 'r')
        # open with json
        rawdata = json.loads(inventoryFile.read())
        # save machine label name (individual) for later variable usage
        labelName = rawdata["machine_label"]
        contents = rawdata['contents']

        # class instances will have to be updated in this loop
        for row in contents:
            for items in row['slots']:
                # create instance of Class
                newMachine = machineData.get(
                    labelName, MachineStatus(labelName))

                # update machine values according to the data
                newMachine.updateBeverages(items["last_stock"])
                newMachine.updateCurrentBeverages(items["current_stock"])
                newMachine.updateIncome(
                    items["item_price"], items["current_stock"], items["last_stock"])
                # MAchine data invididual labels as the keys , values will be the instance of the class
                machineData[labelName] = newMachine
        # update ppercentages because cant intiate percentages other way , divide by zero error
        newMachine.updatePercentages()
        # print labels from class instead of reading values from object again
        newMachine.printLabel()

    # ***********TO SEE THAT DICTIONARY OBJECT WAS CREATED, UNHIGHLIGHT THIS COMMENT LINE***************
    #print("Dictionary Created", machineData)


def inventoryReport():
    inventoryFileNames = ["REID_1F_20171004.json",
                          "REID_2F_20171004.json", "REID_3F_20171004.json"]
    inventoryDict = {}

    for inventoryFileName in inventoryFileNames:
        inventoryFile = open(inventoryFileName, 'r')
        rawdata = json.loads(inventoryFile.read())
        contents = rawdata['contents']

        for row in contents:
            for slot in row['slots']:
                itemName = slot['item_name']
                # variable of dictionary that adds an item that was no previouslt on the list, 2 parameters will pass in
                inventoryItem = inventoryDict.get(
                    itemName, InventoryItem(itemName))  # class ppass in item name , self generates name
                # update the class
                inventoryItem.addToStocked(slot['last_stock'])
                inventoryItem.addToInStock(slot['current_stock'])
                inventoryItem.incrementSlots()
                # save to dict, key is item name , value is a class
                inventoryDict[itemName] = inventoryItem

    sortChoice = ''
    inventoryItemsList = list(inventoryDict.values())
    while sortChoice != 'r':
        sortChoice = input(
            'Sort by (n)ame, (p)ct sold, (s)tocking need, or (r) to return to selection menu: ')
        if sortChoice == 'n':
            inventoryItemsList.sort(key=InventoryItem.getName)
        elif sortChoice == 'p':
            inventoryItemsList.sort(key=InventoryItem.getSoldPct)
            inventoryItemsList.reverse()
        elif sortChoice == 's':
            inventoryItemsList.sort(key=InventoryItem.getStockNeed)
            inventoryItemsList.reverse()

        print('Item Name            Sold     % Sold     In Stock Stock needs')
        for item in inventoryItemsList:
            print('{:20} {:8} {:8.2f}% {:8} {:8}'.format(item.getName(), item.getNumberSold(
            ), item.getSoldPct() * 100, item.getNumberInStock(), item.getStockNeed()))
        print()


# machineReport()
main()
