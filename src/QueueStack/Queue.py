from Node import Node 
from LinkedList import LinkedList
class Queue():
    #constructor for queue class 
    def __init__(self):
        self.__head = self.__tail = None
        self.__count = 0
    
    #enqueues a node to the back of the queue
    def enqueue(self, x):
        temp = Node(x)
        
        if self.__head == None:
            self.__head = temp
            self.__tail = temp
        elif self.isFull() == True:
            return 
        else: 
            current = self.__head
            while current.next != None:
                current = current.next 
            current.next = temp 
            self.__tail = current.next
        self.__count += 1
    
    #removes a node from the FRONT of the list
    def dequeue(self):
        if self.isEmpty():
            return 
        temp = self.__head 
        self.__head = temp.next 
        
        if self.__head == None:
            self.__tail = None 
    
    #checks to see if queue is empty 
    def isEmpty(self):
        return self.__head == None 
    
    ''' To check if the stack is full I just set the max stack size to 50 '''
    def isFull(self):
        if self.__count == 50:
            return True 
        else:
            return False 
    
    #clears the stack 
    def clear(self):
        i = self.dequeue()
        while i != None:
            i = self.dequeue()
        print("Queue cleared")
        return 
    
    #function I made to get the front of the queue - used to dequeue nodes
    def getHead(self):
        return self.__head.data
    
    #returns the data from the tail of the queue
    def poll(self):
        while self.__tail.next != None:
            self.__tail.next = self.__tail.next 
        return self.__tail.data
        