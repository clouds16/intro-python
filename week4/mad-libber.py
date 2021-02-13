import random

person  = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")

class Song:
    def __init__(self, person, verb ,  place):
        self.verblist = ['ate', 'slept', 'asked', "blushed"]
        self.nounslist = ['Beard', 'Banana', "Refrigerator", "Kangaroo"]
        self.verb = verb
        self.place = place
        self.person = person

    def startSong(self):
        return "Twinkle , Twinkle little {0} \nhow i {1} what you are\nUp above the {2} so high\nLike a {0} in the {2}"
    
    def secondVerse(self):
        return "\n\nWhen the blazing {0} is gone\nWhen {2} shines upon\nThen you {1} your little {0}\nTwinkle Twinkle all the night\nTwinkle Twinkle litttle {0}"

# class WordGenerator:
#     def __init__(self, verbs, nouns):
#         self.verbs =  verbs
#         self.nouns = nouns

#     def getNouns(self):
#         return self.nouns[random.randint(0,len(self.nouns)-1)]

#     def getVerbs(self):
#         return self.verbs[random.randint(0,len(self.verbs)-1)]

song = Song(person, verb, place)
print(song.startSong().format(song.person, song.verb, song.place))
print(song.secondVerse().format(song.person, song.verb, song.place))

#randword = WordGenerator(song.verblist, song.noun)
# print(singsong.format(randword.getNouns(), randword.getVerbs(), randword.getNouns(), randword.getNouns(), randword.getNouns() )) 
# print(singverse.format(randword.getNouns(), randword.getNouns(), randword.getVerbs(), randword.getNouns(), randword.getNouns() )) 