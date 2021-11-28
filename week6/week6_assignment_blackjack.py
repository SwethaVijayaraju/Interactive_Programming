# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
question = "Hit or Stand?"
outcome = ''
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        if pos[1] > 300:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            if dealer_first_card:
                card_loc = (CARD_BACK_CENTER[0] + 72, CARD_BACK_CENTER[1])
                canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            else:
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
                canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
                
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        ans = 'Hand contains '
        for i in range(len(self.cards)):
            ans += self.cards[i].__str__() + ' '
        return ans

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        hand_value = 0
        ace = 0
        for card in self.cards:
            rank = card.get_rank()
            hand_value += VALUES[rank] 
            if rank == 'A':
                ace += 1
        if ace != 0 and (hand_value + 10) <= 21:       
            return hand_value + 10
        return hand_value          
           
    def draw(self, canvas, pos):
        global new_player, dealer, dealer_first_card
        if stand:
            dealer_first_card = False
        else:
            dealer_first_card = True
        for item in self.cards:
            card = Card(item.get_suit(), item.get_rank())
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0]
            dealer_first_card = False
        
       

# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
                for rank in RANKS:
                    self.cards.append(suit+rank)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):  
        card = self.cards.pop()
        return Card(card[0], card[1])
    
    def __str__(self):
        str_statement = ''
        for card in self.cards:
            str_statement += card + ' '            
        return 'Deck contains ' + str_statement
    
#define event handlers for buttons
def deal():
    global score, outcome, hand_value, stand, outcome, in_play, test_deck, new_player, dealer, in_play, question
    if in_play:
        outcome = 'Dealer wins!'
        score -= 1
        question = 'New deal?'
        in_play = False
    else:    
        question = "Hit or Stand?"
        outcome = ''
        stand = False
        in_play = True
        test_deck = Deck()
        test_deck.shuffle()
        # print test_deck
        new_player = Hand()
        dealer = Hand()
        for i in range(2):
            new_player.add_card(test_deck.deal_card())        
            dealer.add_card(test_deck.deal_card())
        hand_value = new_player.get_value()
    # print new_player
    # print dealer
    
def hit():
    global test_deck, new_player, dealer, in_play, score, outcome, question, hand_value, stand
    if hand_value <= 21 and in_play:
        new_player.add_card(test_deck.deal_card())
        hand_value = new_player.get_value()
        if hand_value > 21:
            outcome = 'You have busted. Dealer wins!'  
            question = 'New deal?'
            in_play = False
            score -= 1
            stand = True
def stand():
    global test_deck, in_play, score, stand, outcome, question
    stand = True
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(test_deck.deal_card())
        if dealer.get_value() > 21:
            outcome = 'Dealer has busted. You won!'
            score += 1
        elif dealer.get_value() == 21:
            outcome = 'Dealer wins!'            
            score -= 1
        else:
            if dealer.get_value() > new_player.get_value():
                outcome = 'Dealer wins!'                
                score -= 1
            elif dealer.get_value() == new_player.get_value():
                outcome = 'Dealer wins!'                
                score -= 1
            else:
                outcome = 'You won!'                
                score += 1
        in_play = False
    question = 'New deal?'
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('BLACKJACK', (220, 50), 30, 'White')
    canvas.draw_text('Score ' + str(score), (500, 100), 24, 'Black')
    canvas.draw_text('Dealer', (50, 100), 24, 'Black')
    canvas.draw_text(outcome, (180, 100), 24, 'Black')
    canvas.draw_text('Player', (50, 380), 24, 'Black')
    canvas.draw_text(question, (180, 380), 24, 'Black')
    canvas.draw_text('Hand value: ' + str(hand_value), (380, 380), 24, 'Black')
    new_player.draw(canvas, [50, 400]) 
    dealer.draw(canvas, [50, 120])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
hand_value = new_player.get_value()
frame.start()

# remember to review the gradic rubric