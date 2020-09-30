class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def setValue(self, value):
        if (value >= 1 and value <= 13):
            self.value = value
        else:
            print("error: card value must be between 1 and 13, check card class.")

    def getValue(self):
        if (self.value == 1):
            self.value = "Ace"
        if (self.value == 11):
            self.value = "Jack"
        if (self.value == 12):
            self.value = "Queen"
        if (self.value == 13):
            self.value = "King"
        return self.value

    def setSuit(self, suit):
        if (suit == "heart" or "spade" or "club" or "diamond"):
            self.suit = suit
        else:
            print("error: card suit must be 1 of 4 strings, check card class.")

    def getSuit(self):
        return self.suit

    def __str__(self):
        v = self.getValue()
        s = self.getSuit()
        text = "{} of {}'s ".format(v, s)
        return text

def newDeck():
    s = 0
    while (s <= 3):
       v = 1
       if (s == 0):
           suit = "heart"
       elif (s == 1):
           suit = "spade"
       elif (s == 2):
           suit = "club" 
       elif (s == 3):
           suit = "diamond"
       while (v <= 13):
           card = Card(v, suit)
           deck = (card,)
           v += 1
       s += 1
    return deck
#def showDeck(deck):
 #   while (deck[]):

def main():
    deck = newDeck()
    print(deck)
    #showDeck(deck)


   


if __name__ == "__main__":
    main()