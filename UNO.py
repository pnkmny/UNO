import os
import sys
import random
import math
import time


# Generating UNO deck of random UNO cards

class Deck:
    colours = ["Red","Green","Yellow","Blue"]
    values = [0,1,2,3,4,5,6,7,8,9,"Draw Two", "Skip", "Reverse"]
    wilds = ["Wild","Wild Draw Four"]    

    def __init__():
        cur_deck = []
        for c in colours:
            for num in values:
                cardVal = "{} {}".format(colour, value)
                deck.append(cardVal)
                if num != 0:
                    deck.append(cardVal)
        for i in range(4): #since there are 4 wilds
            deck.append(wilds[0])
            deck.append(wilds[1])
    
    def draw(self, n):
        return self.deck.pop()
    
    def shuffle(self):
            random.shuffle(self.deck)   
            
class Hand:
    def __init__(self, deck=None, num_cards=0):
        self.hand = []
        if deck != None:
            self.pop
    def num_of_cards(self):
            return len(self.hand) 
    
    def add_card(self, card):
        self
        
        
def showHand(player, playerHand):
    print("Player {}'s Turn".format(player+1))
    print("Your Hand")
    print("------------------")
    y = 1
    for card in playerHand:
        print("{}) {}".format(y,card))
        y+=1
    print("")
    
class Player:
    
    # draw_cards(n): draws n cards from the top of the deck
    def draw_cards(n):
        cards = []
        for x in range(n):
            cards.append(deck.pop())
        return cards
            
