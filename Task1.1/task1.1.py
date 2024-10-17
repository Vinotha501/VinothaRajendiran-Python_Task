# Implement a Custom Data Structure (Linkedlist, Stack, Queue)

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class linkedlist :
    def __init__(self) :
        self.head = None

    def printlist(self):
        printdata = self.head
        while printdata is not None :
            print (printdata.data)
            printdata = printdata.ref

# insertion at beginning
    # Time Complexity  : O(1), No traversal
    # Space Complexity : O(1), New node created.

    def AtBegining(self,newdata):
      NewNode = Node(newdata)
      NewNode.ref = self.head
      self.head = NewNode

# insertion at the end
    # Time Complexity  : O(n), Requires traversal from head to last node.
    # Space Complexity : O(1), New node created.

    def AtEnd(self,newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while (last.ref):
            last = last.ref
        last.ref = NewNode

# delete node
    # Time Complexity  : O(n), Traverses the list to find node.
    # Space Complexity : O(1), Only few pointers are used.
  
    def delete_node(self, removekey):
        head=self.head

        if (head is not None):
            if (head.data == removekey):
                self.head = head.ref
                head = None
                return
        while (head is not None):
            if head.data == removekey:
                break
            prev = head
            head = head.ref
        if (head == None):
            return
        prev.ref = head.ref
        head = None

# find node
    # Time Complexity  : O(n), Check each node sequentially.
    # Space Complexity : O(1), Only few pointers used.

    def find_node(self, search):
        temp = self.head
        found = 0
        i = 0

        if (temp != None):
            while (temp != None):
                i+= 1
                if (temp.data == search):
                   found+= 1
                   break
                temp = temp.ref

            if (found == 1):
                print (search, "is found in Node")
            else:
                print(search, "is not found in Node")
        else:
            print ("This is an empty list")

# reverse list
    # Time Complexity  : O(n), Traverses each node to reverse the link.
    # Space Complexity : O(1), Only few pointers used.

    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.ref
            current.ref = prev
            prev = current
            current = next
        self.head = prev
          
list = linkedlist()
list.head = Node ("Feb")
l2 = Node ("March")
l3 = Node ("April")

# link first Node to second node
list.head.ref = l2

# link second Node to third node
l2.ref = l3


# Stack
class Stack:
    def __init__(self) :
        self.head = None
        self.size = 0

    # Time Complexity  : O(1), Add new node without traversal.
    # Space Complexity : O(1), New node created.   
    def push (self, data):
        new_node = Node(data)
        if self.head :
            new_node.ref = self.head
        self.head = new_node
        self.size+= 1

    # Time Complexity  : O(1), Removes top node, no traversal.
    # Space Complexity : O(1), Only few pointers used.
    def pop(self):
        if self.isEmpty():
            return ("Stack is empty")
        popped_node = self.head
        self.head = self.head.ref
        return popped_node.data
    
    # Time Complexity  : O(1), Accesses top node, no traversal.
    # Space Complexity : O(1), Only few pointers used.
    def peek(self):
        if self.isEmpty():
            return ("Stack is empty")
        return self.head.data
    
    def isEmpty(self):
        return self.size == 0
    
    def display(self):
        temp = self.head
        print ("Stack:",end=" ")
        while temp:
            print(temp.data,end=", " if temp.ref else"\n")
            temp = temp.ref

    
myStack = Stack()
myStack.push(10)
myStack.push(50)
myStack.push(20)
myStack.push(80)

# Queue
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    # Time Complexity  : O(1), Adds a new node without traversal.
    # Space Complexity : O(1), New node created.
    def enqueue (self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length+= 1
            return
        self.rear.ref = new_node
        self.rear = new_node
        self.length+= 1
    
    # Time Complexity  : O(1), Removes front node without traversal.
    # Space Complexity : O(1), Only few pointers updated.
    def dequeue (self):
        if self.isEmpty():
            return ("Queue is empty")
        temp = self.front
        self.front = temp.ref
        self.length-= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    # Time Complexity  : O(1), Accesses front node without traversal.
    # Space Complexity : O(1), Only few pointers checked.
    def peek (self):
        if self.isEmpty():
            return ("Queue is empty")
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0

    def printqueue (self):
        temp =  self.front
        while temp:
            print (temp.data, end=" ")
            temp = temp.ref
        print()

# Time Complexity  : O(n log n), collect values in a list & sort them.
# Space Complexity : O(1), create temporary list & hold values before sorting.
def sort_stack(stack):
      stack_list = []
      temp = stack.head
      while temp:
        stack_list.append(temp.data)
        temp = temp.ref
      stack_list.sort()
      return stack_list


myqueue = queue()

myqueue.enqueue("A")
myqueue.enqueue("B")
myqueue.enqueue("C")
myqueue.enqueue("D")


# linked list
print("Linked list:")
list.printlist()

print("\nInsertion at beginning:")
list.AtBegining("Jan")
list.printlist()

print("\nInsertion at End:")
list.AtEnd("Dec")
list.printlist()

print("\nDeletion :")
list.delete_node("Feb")
list.printlist()

print("\nFind node:")
list.find_node("April")


# reversed list
print ("\nLinked list before reversing:")
list.printlist()
print("\nLinked list after reversing:")
list.reverse_list()
list.printlist()
print("___________________________\n")

#stack
myStack.display()
print ("Pop:", myStack.pop())
print  ("Peek:", myStack.peek())

print("\nOriginal Stack:")
myStack.display()
print("Sorted Stack:", sort_stack(myStack))

print("___________________________")
# Queue
print ("\nQueue:", end='')
myqueue.printqueue()

print ("Dequeue:", myqueue.dequeue())
print ("Peek:", myqueue.peek())







         
