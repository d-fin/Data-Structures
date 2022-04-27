from Node import Node 

class LinkedList():
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__capacity = 15
        self.__size = 0
    
    def add(self, x):
        newNode = Node(x)
        if self.__head == None:
            self.__head = newNode
        else:
            current = self.__head
            while current.next:
                current = current.next 
            current.next = newNode   
        self.__size += 1 
    
    def remove(self):
        self.__head = self.__head.next
        self.__size -= 1