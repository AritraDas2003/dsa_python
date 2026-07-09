from array import * 
 
MAX = 5 
 
class deque_array: 
    deque = array('i', [0, 0, 0, 0, 0]) 
    rear = -1 
    front = -1 
 
    def insertion_rear_end(self, n): 
        if self.rear == MAX - 1: 
            print("Insertion Not Possible") 
        else: 
            self.rear += 1 
            self.deque[self.rear] = n 
            print("One item added") 
 
    def insertion_front_end(self, n): 
        if self.front == -1: 
            print("Insertion Not Possible") 
        else: 
            self.deque[self.front] = n 
            self.front -= 1 
            print("One item added") 
 
    def deletion_front_end(self): 
        if self.rear == self.front: 
            print("Empty deque") 
        else: 
            self.front += 1 
            n = self.deque[self.front] 
            print("Deleted item =", n) 
 
    def deletion_rear_end(self): 
        if self.rear == self.front: 
            print("Empty deque") 
        else: 
            n = self.deque[self.rear] 
            self.rear -= 1 
            print("Deleted item =", n) 
 
    def display(self): 
        if self.rear == self.front: 
            print("Empty Queue") 
        else: 
            print("The deque is given below:") 
            i = self.front + 1 
            while i <= self.rear: 
                print(self.deque[i]) 
                i += 1 
 
# Create object 
dq = deque_array() 
 
# Menu-driven program 
while True: 
    print("\n**** Main Menu ****") 
    print("1. INSERTION REAR END") 
    print("2. INSERTION FRONT END") 
    print("3. DELETION FRONT END") 
    print("4. DELETION REAR END") 
    print("5. DISPLAY") 
    print("0. EXIT") 
 
    ch = int(input("Enter Your Choice: ")) 
 
    if ch == 1: 
        n = int(input("Enter data: ")) 
        dq.insertion_rear_end(n) 
 
    elif ch == 2: 
        n = int(input("Enter data: ")) 
        dq.insertion_front_end(n) 
 
    elif ch == 3: 
        dq.deletion_front_end() 
 
    elif ch == 4: 
        dq.deletion_rear_end() 
 
    elif ch == 5: 
        dq.display() 
    elif ch == 0: 
        break 
    else: 
        print("Wrong Input")