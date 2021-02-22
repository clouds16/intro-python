import random as r


class Dice:
    def __init__(self):
        self.numdice = 2  # number of dice
        self.numfaces = 6

    def rollDice(self):
        diceRolls = []
        for i in range(self.numdice):
            roll = r.randint[1, self.numfaces]
        return diceRolls


def main():

    count = 0
    dice = Dice()
    diceroll = dice.rollDice()
    usersum = int(input("Roll until what sum"))
    rolls = []

    while True:
        if usersum < 1*dice.numdice or usersum > 6*dice.numdice:
            print("please choose a values between 2 and 12")
        else:
            break

    while True:
        dice = Dice()
        diceroll = dice.rollDice()

        if diceroll != usersum:
            print(diceroll, sum(diceroll))
            rolls.append(diceRolls)
        else:
            print("done ", len(rolls))
            break


main()
