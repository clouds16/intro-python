def main():
    print("\nWelcome to the Golf Club Helper! \nTell me your situation, and I will recommend a club\n")
    promptyorn = str(input("Did you hit it on the green (y/n) ? "))
    prompt_distance = int(input("How far is the ball from the hole? \n"))
    logicloop(promptyorn, prompt_distance)

def logicloop(yorn, distance):
    if yorn == 'y':
        print("I recommend a Putter ")
        
        
    else :
        if distance >= 200 :
            print("i recoommend a driver")
        elif distance < 200 and distance >=140:
            print("I reccomend a 5 Iron")
        elif distance >= 100 and distance <140 :
            print("I recommend a 9 iron")
        else :
            print(" you should use a wedge")

main()