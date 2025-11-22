#queue in oop

class Queue:
  # this is a  constuctor
  def __init__(self,maxSize):
    self.items = []
    self.maxSize = maxSize

  # these are our methods
  def enqueue(self,item):
    if self._isFull():
      print("Queue is full")
    else:
      self.items.append(item)
      print(item," has been added to the queue")
  def dequeue(self):
    if self._isEmpty():
      print("Queue is empty")
    else:
      print("Here you go, have one of these...",self.items[0])
      return self.items.pop(0)  
  def _isFull(self):
    if len(self.items) == self.maxSize:
      return True
    else:
      return False
  def _isEmpty(self):
    if len(self.items) == 0:
      return True
    else:
      return False
  def showFront(self):
    print(self.items[0], "is at the front")
  def showQueue(self):
    print(self.items)
