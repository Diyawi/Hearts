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

	def addCard(self, card):
		self.hand.append(card)

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

def Round(number):
	deck.shuffle()

	if number % 4 == 1:
		spam()
		print(p1)
		print("Choose three cards to pass left to Player 2 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p2)
		print("Choose three cards to pass left to Player 3 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p3)
		print("Choose three cards to pass left to Player 4 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p4)
		print("Choose three cards to pass left to Player 1 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

	elif number % 4 == 2:
		spam()
		print(p1)
		print("Choose three cards to pass right to Player 4 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p4, a, b, c)

		spam()
		print(p2)
		print("Choose three cards to pass right to Player 1 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p3)
		print("Choose three cards to pass right to Player 2 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p4)
		print("Choose three cards to pass right to Player 3 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

	elif number % 4 == 3:
		spam()
		print(p1)
		print("Choose three cards to pass right to Player 4 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p4, a, b, c)

		spam()
		print(p2)
		print("Choose three cards to pass right to Player 1 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p3)
		print("Choose three cards to pass right to Player 2 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)

		spam()
		print(p4)
		print("Choose three cards to pass right to Player 3 (input format: AS AD AH): ")
		a, b, c = input().strip().split(' ')
		passCard(p1, p2, a, b, c)
	else:
		pass

	#13 tricks

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

#Game()


 
"""
shit to do for the game itself:
round(roundNumber, has2C):
Show scores of each player
deal cards to each player
**check round % 4
**ask each player in turn what cards they want to give

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