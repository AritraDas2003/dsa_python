from array import *

MAX = 5

class LinearQueue:
  # both forms below create the same array when MAX == 5
  queue = array('i', [0,0,0,0,0])

  rare = -1
  front = -1


  def enqueue(self, item):
    if (self.rare == MAX-1):
      print("Quque Overflow")
    else:
      self.rare = self.rare +1
      self.queue[self.rare] = item
      print("Item inserted", item)

  def dequeue(self):
    if (self.rare == self.front):
      print("Queue is empty")
    else:
      self.front = self.front+1
      item = self.queue[self.front]
      print("Item deleted: ", item)

  def display(self):
    if (self.rare == self.front):
      print("Queue is empty/ under flow") # same as underflow
    else:
      print("Queue elements are :")
      i = self.front + 1
      while(i <= self.rare):
        print(self.queue[i])
        i += 1

q = LinearQueue()


while True:
  print("*****MENU*****")
  print("1 Enqueue")
  print("2 Dequeue")
  print("3 Display")
  print("4 Exit")

  choice = int(input("Enter your choice"))

  if (choice == 1):
    item = int(input("Enter an Item to insert"))
    q.enqueue(item)
  elif(choice == 2):
    q.dequeue()
  elif(choice == 3):
    q.display()
  elif(choice == 4):
    break
