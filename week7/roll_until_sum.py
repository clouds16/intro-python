import random as r


class Dice:
    def __init__(self):
        self.sides = 6

    def singleRoll(self):
        return (r.randint(1, self.sides))

    def doubleRoll(self):
        return [r.randint(1, self.sides), r.randint(1, self.sides)]


def main():

    myDice = Dice()
    message = "Roll: {} and {} , sum is {}"
    tries = []
    print("This program rolls two 6-sided dice until their sum is a given taget value\n")

    while True:
        target_sum = int(input("Enter the target sum to roll for: "))
        if target_sum < 2 or target_sum > 12:
            print("please enter a number between 2 and 12")
        else:
            break

    while True:
        double_roll = myDice.doubleRoll()

        if sum(double_roll) != target_sum:
            tries.append(double_roll)
            formatmessage = message.format(
                double_roll[0], double_roll[1], sum(double_roll))
            print(formatmessage)

        else:
            tries.append(double_roll)
            formatmessage = message.format(
                double_roll[0], double_roll[1], sum(double_roll))
            print(formatmessage)
            break

    print("\nGot it in ", len(tries), "rolls! ")


main()
