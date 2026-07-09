from array import * 
 
MAX = 5 
 
class queue_array: 
    queue = array('i', [0, 0, 0, 0, 0]) 
    rear = -1 
    front = -1 
 
    def insertion(self, n): 
        if self.rear == MAX - 1: 
            print("QUEUE OVERFLOW") 
        else: 
            self.rear += 1 
            self.queue[self.rear] = n 
            print("One item added") 
 
    def deletion(self): 
        if self.rear == self.front: 
            print("Empty Queue") 
        else: 
            self.front += 1 
            n = self.queue[self.front] 
            print("Deleted item =", n) 
 
    def display(self): 
        if self.rear == self.front: 
            print("Empty Queue") 
        else: 
            print("The Queue is given below:") 
            i = self.front + 1 
            while i <= self.rear: 
                print(self.queue[i]) 
                i += 1 
 
# Create object 
q = queue_array() 
 
# Menu-driven program 
while True: 
    print("\n**** Main Menu ****") 
    print("1. INSERTION") 
    print("2. DELETION") 
    print("3. DISPLAY") 
    print("0. EXIT") 
 
    ch = int(input("Enter Your Choice: ")) 
 
    if ch == 1: 
        n = int(input("Enter data: ")) 
        q.insertion(n) 
 
    elif ch == 2: 
        q.deletion() 
 
    elif ch == 3: 
        q.display() 
 
    elif ch == 0: 
        break 
 
    else: 
        print("Wrong Input")