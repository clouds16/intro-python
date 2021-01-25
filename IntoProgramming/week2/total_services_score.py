def scoretracker(count):
    values =[]
    for i in range(count):
        dayscore = float(input("Enter the score for day " + str(i+1) + " : "))
        values.append(dayscore)
    total = sum(values)
    print("The total score of the", count , "days is : ", total)

def main():
    prompt_counter = int(input('How many days of score? '))
    scoretracker(prompt_counter)  

if __name__ == '__main__':
    main()
    


