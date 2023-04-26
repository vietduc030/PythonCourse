# Implement a class to represent a deck of playing cards.
#  This class should be able to shuffle the 
# deck and deal cards to players.
import random 
class Deck:
    
    def __init__(self):
        """Creates a list of all cards in a list"""
        self.decklist=[]
        self.listcards=["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        self.symbols=["Heart","Spade","Diamond","Club"] 
        for x in range(len(self.symbols)):
            for y in range(len(self.listcards)):
                self.decklist.append(self.listcards[y]+" of "+self.symbols[x])
    
    """Draw a card of the deck, deletes the card from list and returns that card as value"""    
    def draw(self):
        
        lucky=random.randint(0,len(self.decklist)-1)  
        draw_card=self.decklist.pop(lucky)   
        return draw_card
    """Shuffle Deck Randomly"""
    def shuffle(self):
        random.shuffle(self.decklist)  #Shuffles the list randomly
            

d=Deck()
p1_starting_hand=[d.draw() for i in range(5)]
d.shuffle()
print(p1_starting_hand)


#
#listcards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
#symbols = ["Heart", "Spade", "Diamond", "Club"] 
#decklist = [card + " of " + symbol for card in listcards for symbol in symbols]


# print(decklist)
