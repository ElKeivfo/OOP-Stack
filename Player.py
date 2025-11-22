#player class

class Player:

  def __init__(self,name):
    self.name = name
    self.hand = []

  def place_hand(self):
    return self.hand.pop()
  
  def getName(self):
    return self.name

  def pick_up_card(self,card):
    self.hand.append(card)

  def show_hand(self):
    print(self.hand)

