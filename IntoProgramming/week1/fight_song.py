def go_team():
    print("Go, team, go! \nDefeat your foe,")

def simply_best():
    print("Simply the best, \nBetter than the rest.")

def space():
    print("\n")

def intro_and_end():
    go_team()
    space()

def midsection():
    go_team()
    simply_best()
    go_team()
    space()

def sing_fight_song():
    n =0
    space()
    intro_and_end()

    while n<2 :
        midsection()
        n=n+1
    
    intro_and_end() 

if __name__ == "__main__":
    sing_fight_song()
