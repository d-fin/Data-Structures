from Node import Node 
from LinkedList import LinkedList 

class Stack():
    # constructor for stack class
    def __init__(self):
        self.__top = None
        
    # push item onto stack
    def push(self, x):
        if self.isFull():
            print("Stack is full")
            return 
        elif self.__top == None:
            self.__top = Node(x)
        else:
            newNode = Node(x)
            newNode.next = self.__top 
            self.__top = newNode 
            
    
    # pops item from top of stack
    def pop(self):
        if self.isEmpty():
            return None 
        else:
            popNode = self.__top
            if self.__top.next == None:
                self.__top = None
                return 
            else:
                self.__top = popNode.next
                return popNode.data
    
    # returns Boolean of whether stack is currently empty
    def isEmpty(self):
        if self.__top == None:
            return True 
        else:
            return False 
    
    # returns Boolean of whether stack is currently full
    def isFull(self):
        i = 0
        temp = self.__top
        if temp == None:
            return 
        while temp != None:
            i += 1
            temp = temp.next
        
        if i == 15:
            print("Stack full")
            return 
        return 
    
    # clears the stack
    def clear(self):
        i = self.pop()
        while i != None:
            i = self.pop()
        print("Stack cleared")
        return 
    
    # looks at the top item of the stack without removing it
    def peek(self):
        if self.isEmpty():
            return None 
        else:
            return self.__top.data
    