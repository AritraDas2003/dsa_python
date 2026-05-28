from array import *
MAX = 5

class DEQueue:
  front  = -1
  rare = -1
  deQueue = array('i',[0,0,0,0,0])

  def insertion_rare_end(self,item):
    if(self.rare == MAX -1):
      print("insertion not possible")
    else:
      self.rare = self.rare + 1
      self.deQueue[self.rare] = item
      print("item inserted: ", item)

  def insertion_front_end(self,item):
    if (self.front == -1):
      print("Insertion not possible")
    else:
      self.deQueue[self.front] = item
      self.front =self.front -1
      print("Item inserted at front ", item)

  def deletion_front_end(self):
    if(self.front == self.rare):
      print("Queue is empty")
    else:
      self.front = self.front + 1
      item = self.deQueue[self.front]
      print("Item Deleted from front: ", item)
  def deletion_rare_end(self):
    if(self.front == self.rare):
        print("Queue is empty")
    else:
        item = self.deQueue[self.rare]
        self.rare = self.rare - 1
        print("Item deleted from rare: ", item)

  def display(self):
    if(self.front == self.rare):
      print("Queue is empty")
    else:
      print("Queue elements are:  ")
      i = self.front + 1

      while i <= self.rare:
        print(self.deQueue[i])
        i = i+1

dq = DEQueue()

while True:
  print("*****Menu*****")
  print("1. Insertion at rare")
  print("2. Insertion at front")
  print("3. Deletion at rare")
  print("4. Deletion at front")
  print("5. Display")
  print("6. Exit")

  ch = int(input("Enter Your choice"))

  if(ch == 1):
    item = int(input("Enter Item to be inserted"))
    dq.insertion_rare_end(item)

  elif(ch == 2):
    item = int(input("Enter Item to be inserted"))
    dq.insertion_front_end(item)
  elif(ch == 3):
    dq.deletion_rare_end()
  elif(ch == 4):
    dq.deletion_front_end()
  elif(ch == 5):
    dq.display()
  elif(ch == 6):
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please try again.")
