import random

class Song:
    def __init__(self):
        self.verbs = ['ate', 'slept', 'asked', 'crashed', "blushed"]
        self.nouns = ['Beard', "Airport", 'Banana', "Refrigerator", "Kangaroo"]

    def startSong(self):
        return "Twinkle , Twinkle little {} \nhow i {} what you are\nUp above the {} so high\nLike a {} in the {} "


class WordGenerator:
    def __init__(self, verbs, nouns):
        self.verbs =  verbs
        self.nouns = nouns

    def getNouns(self):
        return self.nouns[random.randint(0,len(self.nouns)-1)]

    def getVerbs(self):
        return self.verbs[random.randint(0,len(self.verbs)-1)]


song = Song()
singsong = Song().startSong()
randword = WordGenerator(song.verbs, song.nouns)


print(singsong.format(randword.getNouns(), randword.getVerbs(), randword.getNouns(), randword.getNouns(), randword.getNouns() )) 
