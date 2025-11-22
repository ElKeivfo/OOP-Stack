#STACK in OOP. 
import random
from Queue import Queue
from Player import Player
values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Clubs","Spade","Hearts","Diamonds"]
cards = []
for value in values:
  for suit in suits:
    card = value+" "+suit
    cards.append(card)
    random.shuffle(cards)
print(cards)


class Stack:

  def __init__(self,maxSize):
    self.items = []
    self.maxSize = maxSize
    self.FrontOfStack = 0
    self.BottomOfStack = 0

  def maxium_size(self,maxSize):
    self.maxSize == len(self.items)
    print(self.maxSize)

  def find_top_of_stack(self):
    print(peek.self.cards)

  def push(self,item):
    if not self.isFull():
      self.items.append(item)


  def pop(self):
    if self.isFull() == False:
      print(self.items.pop())

  def isFull(self):
    if self.maxSize == len(self.items):
      print("Is full. ")
      return True
    else:
      return False

  def isEmpty(self):
    if maxSize == 0:
      print("Is empty. ")

  def show_stack(self):
    print(self.items)


deck = Queue(52)#cards.maximum_size()
for card in cards:
  deck.enqueue(card)

players = []
for i in range(4):
  name = input("Please enter player name: ")
  players.append(Player(name))

for player in players:
  print("Player name is : ",player.getName())

for player in players:
  for i in range(7):
    player.pick_up_card(deck.dequeue())

for player in Players():
  print("Player ",player.getName(),"hand")
  players.show_hand()
#from stack import stack
#from queue import Queue
