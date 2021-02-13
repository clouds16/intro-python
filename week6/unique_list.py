class Sequence:
    def createList(self):
        usernumbers = []
        usernumbers.append((int(input("Enter the first number: "))))
        while True:
            userinput = int(input("Next: "))
            if userinput != -1 :
                usernumbers.append(userinput)
            else: 
                break
        print(usernumbers)
        return usernumbers
    
    def sequenceCheck( self, userList):
        
        if len(userList) == len(set(userList)):
            print("No Duplicates found" )
        else: 
            print("Duplicates found")

    def run(self):
        self.sequenceCheck(self.createList())

Sequence().run()
