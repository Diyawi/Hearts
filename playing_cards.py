from enum import Enum
import random

# playingcardmodule
# CS 5 C

class PlayingCardSuit(Enum):
    """
    This enumeration allows a card to have a suit.
    """
    clubs = "clubs"
    diamonds = "diamonds"
    hearts = "hearts"
    spades = "spades"

    def __str__(self):
        """
        String representation of a PlayingCardSuit.
        """
        return self.value

    def repChar(self):
        """
        Character representation of a PlayingCardSuit.
        """
        return self.name[0].upper()

    def matchChar(char):
        """
        Method to match a character to the first letter of the string
        representation of a PlayingCardSuit and return the instance of
        the PlayingCardSuit. This is a convenience method to allow the
        constructor of the PlayingCard class to accept a string.
        """
        if char[0].upper() == "C":
            return PlayingCardSuit.clubs
        if char[0].upper() == "D":
            return PlayingCardSuit.diamonds
        if char[0].upper() == "H":
            return PlayingCardSuit.hearts
        if char[0].upper() == "S":
            return PlayingCardSuit.spades

    def isSameColor(self, other):
        """
        Method to check whether one suit is the same as another.
        """
        selfColor = "red"
        otherColor = "red"
        if self in [PlayingCardSuit.clubs, PlayingCardSuit.spades]:
            selfColor = "black"
        if other in [PlayingCardSuit.clubs, PlayingCardSuit.spades]:
            otherColor = "black"
        return selfColor == otherColor

class PlayingCardFace(Enum):
    """
    This enumeration allows a PlayingCard to have a face.
    """
    ace = 14
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    jack = 11
    queen = 12
    king = 13

    def __str__(self):
        """
        String representation of a PlayingCardFace.
        """
        return str(self.value)

    def repWord(self):
        """
        The word for the face of a PlayingCard.
        """
        words = ("ace", "two", "three", "four", "five", "six",
                 "seven", "eight", "nine", "ten", "jack", "queen",
                 "king")
        return words[self.value - 1]

    def repChar(self):
        """
        Character representation of a PlayingCardFace.
        """
        if self.value == PlayingCardFace.ace.value:
            return "A"
        elif self.value == PlayingCardFace.ten.value:
            return "T"
        elif self.value == PlayingCardFace.jack.value:
            return "J"
        elif self.value == PlayingCardFace.queen.value:
            return "Q"
        elif self.value == PlayingCardFace.king.value:
            return "K"
        else:
            return str(self.value)

    def matchValue(value):
        """
        Method to match a character to the first letter of the string
        representation of a PlayingCardSuit and return the instance of
        the PlayingCardSuit. This is a convenience method to allow the
        constructor of the PlayingCard class to accept a string.
        """
        for face in PlayingCardFace:
            if face.value == value:
                return face

class PlayingCard:
    '''
    A PlayingCard represents a standard card in a
    standard 52-card deck.
    '''

    def __init__(self, suit = PlayingCardSuit.clubs,
                 face = PlayingCardFace.ace):
        """
        Constructs a PlayingCard. The suit can be a PlayingCardSuit or
        a one-character string that matches the first letter of the
        defined suits. The face value can be a PlayingCardFace or a
        number that maps to the defined face values.
        """
        if suit:
            if type(suit) == PlayingCardSuit:
                self.suit = suit
            elif type(suit) == str:
                self.suit = PlayingCardSuit.matchChar(suit)
        if face:
            if type(face) == PlayingCardFace:
                self.face = face
            elif type(face) == int:
                self.face = PlayingCardFace.matchValue(face)

    def __str__(self):
        """
        String representation of a PlayingCard.
        """
        return self.face.repWord() + " of " + str(self.suit)

    def __repr__(self):
        """
        Short representation of a PlayingCard.
        """
        return self.face.repChar()+self.suit.repChar()

    def __lt__(self, other):
        """
        Method to check if the value of one card is less than another
        card's value.
        """
        return self.face.value < other.face.value

    def __gt__(self, other):
        """
        Method to check if the value of one card is greater than
        another card's value.
        """
        return self.face.value > other.face.value

    def __eq__(self, other):
        """
        Method to check if the value of one card is equal to another
        card's value.
        """
        return self.face.value == other.face.value

    def __hash__(self):
    	return self.face.value

class PlayingCardDeck:
    """
    A playing card deck used in many card games.
    """
    def __init__(self):
        """
        Constructs a PlayingCardDeck in a standard manner with one
        card each of each suit matching each face.
        """
        self.deck = []
        for suit in PlayingCardSuit:
            for face in PlayingCardFace:
                self.deck.append(PlayingCard(suit, face))

    def shuffle(self):
        """
        Shuffles the deck.
        """
        random.shuffle(self.deck)

    def deal(self):
        """
        Removes the last card in the deck and returns it.
        """
        return self.deck.pop()

    def __str__(self):
        """
        String representation of the deck.
        """
        stringer = ""
        breaker = 13

        i = 0
        for card in self.deck:
            if i != 0:
                stringer += " "
            stringer += repr(card)
            i += 1
            if breaker <= i:
                i = 0
                stringer += "\n"
        return stringer

    def __repr__(self):
        """
        Short representation of the deck.
        """
        return str(self)

deck = PlayingCardDeck()
deck.shuffle()

class Hand:
	"""
    Hand of a Player.
    """

	def __init__(self):
		"""
		Initializes player's hand.
		"""
		self.hand = []
		for x in range(0, 13):
			self.hand.append(deck.deal())
		self.hand.sort()

	def __contains__(self, card):
		return True

	def __str__(self):
		"""
			String representation of the deck.
		"""
		stringer = ""

		i = 0
		for card in self.hand:
			if i != 0:
				stringer += " "
			stringer += repr(card)
			i += 1
		return stringer

	def __repr__(self):
		return str(self)

	def playCard(self, card):
		"""
		returns the value of a card and removes that card from the hand. Accepts string values
		"""
		for i in self.hand:
			if repr(i) == card:
				self.hand.remove(i)
				return i
		self.hand.sort()

	def addCard(self, card):
		self.hand.append(card)
		self.hand.sort()

class Player:
	"""
	Player in the game. Includes name, hand, score and if they are going first
	"""

	def __init__(self, name, hand, score, isFirst = False):
		self.name = name
		self.hand = hand
		self.score = int(score)
		if isFirst:
			self.isFirst = True
		else:
			self.isFirst = False

	def __str__(self):
		return str(self.name) + "\nScore: " + str(self.score) + "\nCards:\n" + str(self.hand)

	def __repr__(self):
		return str(self)

	def starts(self):
		self.isFirst = True

	def notStart(self):
		self.isFirst = False

def Round(number):

	deck.shuffle()

	if number % 4 == 1:
		spam()
		print(p1)
		print("Choose three cards to pass left to " + p2.name + " (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p2)
		print("Choose three cards to pass left to " + p3.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p2, p3, a, b, c)

		spam()
		print(p3)
		print("Choose three cards to pass left to " + p4.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p3, p4, a, b, c)

		spam()
		print(p4)
		print("Choose three cards to pass left to " + p1.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p4, p1, a, b, c)

	elif number % 4 == 2:
		spam()
		print(p1)
		print("Choose three cards to pass right to " + p4.name + " (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p4, a, b, c)

		spam()
		print(p2)
		print("Choose three cards to pass right to " + p1.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p2, p1, a, b, c)

		spam()
		print(p3)
		print("Choose three cards to pass right to " + p2.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p3, p2, a, b, c)

		spam()
		print(p4)
		print("Choose three cards to pass right to " + p3.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p4, p3, a, b, c)

	elif number % 4 == 3:
		spam()
		print(p1)
		print("Choose three cards to pass right to " + p3.name + " (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p3, a, b, c)

		spam()
		print(p2)
		print("Choose three cards to pass right to " + p4.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p2, p4, a, b, c)

		spam()
		print(p3)
		print("Choose three cards to pass right to " + p1.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p3, p1, a, b, c)

		spam()
		print(p4)
		print("Choose three cards to pass right to " + p2.name + " (input format: AS AD AH): ")
		print("You cannot choose: " + a + " " + b + " " + c)
		a, b, c = input().strip().split(' ')
		passCard(p4, p2, a, b, c)
	else:
		pass

	card = PlayingCard(PlayingCardSuit.clubs, PlayingCardFace.two)
	if card in p1.hand:
		p1.starts()
	elif card in p2.hand:
		p2.starts()
	elif card in p3.hand:
		p3.starts()
	elif card in p4.hand:
		p4.starts()

	for i in range(0, 13):
		Trick(p1, p2, p3, p4)
		pass

def Game():
	i = 1
	while p1.score < 100 and p2.score < 100 and p3.score < 100 and p4.score < 100:
		Round(i)
		i += 1

def passCard(playerFrom, playerTo, card1, card2, card3):
	"""
	passes 3 cards from one player to another
	"""
	playerTo.hand.addCard(playerFrom.hand.playCard(card1))
	playerTo.hand.addCard(playerFrom.hand.playCard(card2))
	playerTo.hand.addCard(playerFrom.hand.playCard(card3))
	
def spam():
	"""
	for adding whitespace
	"""
	for i in range(0, 100):
		print("*")

def Highest(card1, card2, card3, card4, suit):
	card = [card1, card2, card3, card4]
	card = [i for i in card if i.suit == suit]

	moreCards = []

	for i in card:
		moreCards.append(i)

	for i in card:
		for j in card:
			if i.face.value < j.face.value:
				if i in moreCards:
					moreCards.remove(i)

	return moreCards[0]

def winner(p1, p2, p3, p4, card1, card2, card3, card4):
	suit = card1.suit
	trick = {repr(card1): p1, repr(card2): p2, repr(card3): p3, repr(card4): p4}
	score = checkScore(card1, card2, card3, card4)
	winningCard = repr(Highest(card1, card2, card3, card4, suit))
	trick.get(winningCard).score += score
	p1.isFirst = False
	p2.isFirst = False
	p3.isFirst = False
	p4.isFirst = False
	#trick.get(winningCard).isFirst = True
	return trick.get(winningCard)

def checkScore(card1, card2, card3, card4):
	cards = [card1, card2, card3, card4]
	score = 0
	for i in cards:
		if i.suit == PlayingCardSuit.hearts:
			score +=1
	return score

def Trick(p1, p2, p3, p4):
	spam()

	if p1.isFirst == True:
		print(p1)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card1 = p1.hand.playCard(input())
		spam()
		print("Cards Played: ") 
		print(repr(card1))
		print(p2)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card2 = p2.hand.playCard(input())
		spam()
		print("Cards Played: ") 
		print(repr(card1))
		print(repr(card2))
		print(p3)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card3 = p3.hand.playCard(input())
		spam()
		print("Cards Played: ") 
		print(repr(card1))
		print(repr(card2))
		print(repr(card3))
		print(p4)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card4 = p4.hand.playCard(input())
		winner(p1, p2, p3, p4, card1, card2, card3, card4).isFirst = True
	elif p2.isFirst == True:
		print(p2)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card2 = p2.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card2))
		print(p3)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card3 = p3.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card2))
		print(repr(card3))
		print(p4)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card4 = p4.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card2))
		print(repr(card3))
		print(repr(card4))
		print(p1)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card1 = p1.hand.playCard(input())
		winner(p2, p3, p4, p1, card2, card3, card4, card1).isFirst = True
	elif p3.isFirst == True:
		print(p3)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card3 = p3.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card3))
		print(p4)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card4 = p4.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card3))
		print(repr(card4))
		print(p1)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card1 = p1.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card3))
		print(repr(card4))
		print(repr(card3))
		print(p2)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card2 = p2.hand.playCard(input())
		winner(p3, p4, p1, p2, card3, card4, card1, card2).isFirst = True
	else:
		print(p4)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card4 = p4.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card4))
		print(p1)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card1 = p1.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card4))
		print(repr(card1))
		print(p2)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card2 = p2.hand.playCard(input())
		spam()
		print("Cards Played: ")
		print(repr(card4))
		print(repr(card1))
		print(repr(card2))
		print(p3)
		print("Pick a card to play, please don't choose an illegal card we don't have error handling haha: ")
		card3 = p3.hand.playCard(input())
		winner(p4, p1, p2, p3, card4, card1, card2, card3).isFirst = True

print("Input name of Player One: ")
name1 = str(input())
print("Input name of Player 2: ")
name2 = str(input())
print("Input name of Player 3: ")
name3 = str(input())
print("Input name of Player 4: ")
name4 = str(input())

p1 = Player(name1, Hand(), 0, False)
p2 = Player(name2, Hand(), 0, False)
p3 = Player(name3, Hand(), 0, False)
p4 = Player(name4, Hand(), 0, False)

a = PlayingCard(PlayingCardSuit.clubs, PlayingCardFace.two)
b = PlayingCard(PlayingCardSuit.clubs, PlayingCardFace.ace)
c = PlayingCard(PlayingCardSuit.clubs, PlayingCardFace.three)
d = PlayingCard(PlayingCardSuit.hearts, PlayingCardFace.ace)


Game()


"""
shit to do for the game itself:
round(roundNumber):

trick (starter, firstDrop, penaltyCards, winner):
see which player has the 2C
designate that player as the starting player
start tricks
prompt each player to drop a card
note what suit is the first drop
error message for illegal moves
note if there are penalty cards
if there are, add to the score of the trick winner
"""