
def main():
    while True:
        print("\nWelcome to the Golf Club Helper! \nTell me your situation, and I will recommend a club\n")
        ballongreen = str(input("Did you hit it on the green (y/n) ? "))
    
        if ballongreen == 'y':
            
            greendistance = int(input("How far is the ball from the hole? "))
            print("\nI recommend a Putter\n\n ")
        
        elif ballongreen == 'n' :

            distance = int(input("How far is the ball from the hole? "))
        
            if distance >= 200 :
                print("\nI recoommend a driver\n\n")
            elif distance < 200 and distance >=140:
                print("\nI reccomend a 5 Iron\n\n")
            elif distance >= 100 and distance <140 :
                print("\nI recommend a 9 iron\n\n")
            else :
                print("\nYou should use a wedge\n\n")
                
        elif ballongreen == 'q':
            break
        
        else :
            print("Please input either (y) for yes or (n) for no or (q) to quit\n\n")


main()