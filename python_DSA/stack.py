class Stack:
    def __init__(self, max_size=5):
        self.max_size = max_size
        self.items = [None] * max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Stack is full. Cannot push.")
        else:
            self.top += 1
            self.items[self.top] = item
            print(item, "pushed into stack.")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            print("Popped item:", value)
            return value

  # Peek and size methods are optional

    def peek(self):
        if self.is_empty():
            print("Stack is empty. Nothing to peek.")
        else:
            print("Top item:", self.items[self.top])
            return self.items[self.top]

    def size(self):
        current_size = self.top + 1
        print("Current size:", current_size)
        return current_size

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (bottom to top):")
            i = 0
            while i <= self.top:
                print(self.items[i])
                i += 1


def menu():
    stack = Stack(5)  # Create a stack with a maximum size of 5

    while True:
        print("\n----- STACK MENU -----")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Size")
        print("7. Display")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to push: ")
            stack.push(item)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            stack.peek()

        elif choice == "4":
            if stack.is_empty():
                print("Stack is empty.")
            else:
                print("Stack is not empty.")

        elif choice == "5":
            if stack.is_full():
                print("Stack is full.")
            else:
                print("Stack is not full.")

        elif choice == "6":
            stack.size()

        elif choice == "7":
            stack.display()

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()