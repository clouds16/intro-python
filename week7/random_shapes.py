import random


class Rectangle:
    def __init__(self, width, height):
        self.name = 'Rectangle'
        self.width = width
        self.height = height
        self.buffer = 20
        self.color_ceiling = 255
        self.point_one = ""
        self.point_two = ""
        self.color_rgb = ""

    def createPoint(self):
        xposition = random.randint(0, self.width)
        yposition = random.randint(0, self.height)
        stringoutput = "{},{}".format(xposition, yposition)

        return stringoutput

    def createColor(self):
        color_one = random.randint(0, 255)
        color_two = random.randint(0, 255)
        color_three = random.randint(0, 255)

        stringoutput = "{},{},{}".format(color_one, color_two, color_three)
        self.color = stringoutput
        return self.color

    def createRandomRectangle(self):
        outputString = "{};{};{};{}".format(
            self.name, self.createPoint(), self.createPoint(), self.createColor())
        return outputString


class Circle:
    def __init__(self, width, height):
        self.name = "Circle"
        self.width = width
        self.height = height
        self.centerpoint = 0
        self.radius = 0
        self.radius_limiter = 50
        self.color = ""

    def createRadius(self):
        radius = random.randint(0, self.radius_limiter)
        return str(radius)

    def createPoint(self):
        xposition = random.randint(0, self.width)
        yposition = random.randint(0, self.height)
        stringoutput = "{},{}".format(xposition, yposition)
        return stringoutput

    def createColor(self):
        color_one = random.randint(0, 255)
        color_two = random.randint(0, 255)
        color_three = random.randint(0, 255)

        stringoutput = "{},{},{}".format(color_one, color_two, color_three)
        self.color = stringoutput
        return self.color

    def createRandomCircle(self):
        outputString = "{};{};{};{}".format(
            self.name, self.createPoint(), self.createRadius(), self.createColor())
        return outputString


def main():
    filename = str(input("Enter the Drwaing file name to create: "))
    shapeCount = int(input("Enter the number of shapes to make: "))

    userfile = open(filename, "w+")

    window_width = 600
    window_height = 400

    for i in range(shapeCount):
        shape = getShape()

        if shape == "Rectangle":
            generateRect = Rectangle(
                window_width, window_height).createRandomRectangle()

            userfile.write(generateRect + "\n")

        else:
            generateCircle = Circle(
                window_width, window_height).createRandomCircle()

            userfile.write(generateCircle + "\n")

    print("Done writing to file!")
    userfile.close()


def getShape():
    shapesCanGenerate = ["Rectangle", "Circle"]
    rand = random.randint(1, len(shapesCanGenerate))

    if rand == 1:
        return shapesCanGenerate[0]
    else:
        return shapesCanGenerate[1]


main()
