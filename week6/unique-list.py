class Sequence:
    def __init__(self):
        # user numbers will be stored in a class variable , accessible by all methods
        self.usernumbers = []

    def createList(self):
        self.usernumbers.append((int(input("Enter the first number: "))))

        while True:
            userinput = int(input("Next: "))
            # check to see that user input is not the break condition
            if userinput != -1:
                self.usernumbers.append(userinput)
            else:
                break

        return self.usernumbers

    def sequenceCheck(self, userList):
        # this comparitor checks if the user list by itself is the same as when it is created into a set, set makes unique list
        # set does not create duplicated in list. if lists comparitors do not match, we know that they are not the same list, thus there are repeating values
        if len(userList) == len(set(userList)):
            #print(userList, set(userList))
            print("The sequence is :", self.usernumbers, "IS Unique ")
            print("No Duplicates found")
            # these return values exit the loop, can be useful for future applications if want to eliminate print values, and have some logic check to see if the list
            # was unique or not
            return False
        else:
            #print(userList, set(userList))
            print("The sequence is :", self.usernumbers, "is NOT unique!")
            print("Duplicates found")
            return True

    # the main method to run logic from other methods
    def run(self):
        self.sequenceCheck(self.createList())


# calling class and method. Can create instance if necessary
Sequence().run()
