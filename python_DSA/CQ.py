from array import *
MAX = 5
class CQueue:
  front =0
  rare = 0
  queue = array('i',[0,0,0,0,0])

  def enqueue(self,item):
    if((self.rare +1 ) %MAX == self.front):
      print("Queue overflow")
    else:
      self.queue[self.rare] = item
      self.rare = (self.rare +1) % MAX
      print("Item inserted",item)

  def dequeue(self):
    if (self.front == self.rare):
      print("Queue underflow")
    else:
      item = self.queue[self.front]
      self.front = (self.front + 1) % MAX
      print("Item Deleted", item)

  def display(self):
    if (self.front == self.rare):
      print("Queue underflow")
    else:
      i = self.front

      while (i != self.rare):
        print(self.queue[i])

        i = (i+1) % MAX
cq = CQueue()

while True:
  print("\n*****MENU*****")
  print("1. Enqueue")
  print("2. Dequeue")
  print("3. Display")
  print("4. Exit")

  ch = int(input("\nEnter your choice"))

  if(ch == 1):
    item = int(input("Enter an Element to be inserted: "))
    cq.enqueue(item)
  elif(ch == 2):
    cq.dequeue()
  elif(ch == 3):
    cq.display()
  elif(ch == 4):
    break
  else:
    print("Invalid input") # optional step... can be removed