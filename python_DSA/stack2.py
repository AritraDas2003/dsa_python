class Stack:

  def __init__(self, max_size =5):
    self.max_size = max_size
    self.items = [None]* max_size
    self.top = -1

  def is_empty(self):
    return self.top == -1

  def is_full(self):
    return self.top ==self.max_size -1

  def push (self,item):

    if self.is_full():
      print("Stack is full. Overflow!")
    else:
      self.top += 1
      self.items[self.top] = item
      print(item, "Pushed in to stack")

  def pop(self):
    if self.is_empty():
      print ("Stack is empty. Underflow!")
    else:
      curr_item = self.items[self.top]
      self.items[self.top] = None
      self.top -= 1
      print("Item popped: ", curr_item)
      return curr_item

  def display(self):
    if self.is_empty():
      print("Stack is empty.")
    else:
      print("stack items bottom to top:")

      i = self.top
      while i >= 0: # >= 0 is used because we also take the bottom elemrnt which is at index 0..  it print s from top to bottom
        print(self.items[i])
        i -= 1

def menu():
    stack = Stack(5)

    while True:
      print("\n ***** STACK MENU *****")
      print("1. Push")
      print("2. Pop")
      print("3. Display")
      print("4. Exit")

      choice  = int(input("Enter your choice: "))

      if choice == 1:
        item = input("Enter item to push: ")
        stack.push(item)

      elif choice == 2:
        stack.pop()

      elif choice == 3:
        if stack.is_empty():
          print("Stack is empty.")
        else:
          stack.display()

      elif choice == 4:
        print ("Exiting...")
        break

      else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
  menu()