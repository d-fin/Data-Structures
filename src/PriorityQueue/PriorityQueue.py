from Node import Node 

class PriorityQueue:
    def __init__(self):
        self.front = None 

    def push(self, val, priority):
        if self.isEmpty() == True: 
            self.front = Node(val, priority)
            return 
        
        else:
            if self.front.priority > priority:
                x = Node(val, priority)
                x.next = self.front 
                return 
            else:
                temp = self.front 
                while temp.next != None:
                    if priority <= temp.next.priority:
                        break 
                    temp = temp.next 
                
                y = Node(val, priority)
                y.next = temp.next 
                temp.next = y 
                return 

    def pop(self):
        if self.isEmpty() == True:
            return False
        else:
            self.front = self.front.next 
            return True 

    def isEmpty(self):
        if self.front == None:
            return True 
        else: return False 