def logic():

    input_phrase = input("\nInput your phrase: ")
    count = int(input("\nHow many times should itbe repeated? "))

    for i in range(count):
        print(str(i+1) + " " + input_phrase)

if __name__ == "__main__":
    logic()
    pass