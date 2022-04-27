from Stack import Stack 
from Queue import Queue 
from LinkedList import LinkedList
from QueueParenthesisChecker import QueueParenthesisChecker 
from StackParenthesisChecker import StackParenthesisChecker

def main():
    ''' Below I declare my variables for the parentheses checker and my stack and queue '''
    checker1 = StackParenthesisChecker()
    checker2 = QueueParenthesisChecker()
    stack = Stack()
    queue = Queue()
    
    userString = None 
    cont = False
    
    while cont == False:
        userString = input("Enter a string or quit to check the strings: ")
        if userString.upper() == "QUIT":
            cont = True 
        else:
            stack.push(userString)
            queue.enqueue(userString)
    print("\n")
    
    ''' Below is my stack implementation and after each parentheses check I pop the item off of the 
    stack and at the end I check to make sure the stack is clear.
     '''
    print("Stack implementation")
    while stack.isEmpty() != True:
        item = stack.peek()
        if checker1.isBalanced(item) == True:
            print(f'The input string {item} has balanced parentheses.')
        else:
            print(f'The input string {item} does not have balanced parentheses.')
        stack.pop()
    stack.clear()
    print("\n")
    
    ''' Below is my queue implementation and I did the same thing as the stack where I check then 
    dequeue the item. At the end I make sure the queue is clear before terminating the program. '''
    print("Queue implementation")
    while queue.isEmpty() != True:
        item = queue.getHead()
        if checker2.isBalanced(item) == True:
            print(f'The input string {item} has balanced parentheses.')
        else:
            print(f'The input string {item} does not have balanced parentheses.')
        queue.dequeue()
    queue.clear()
            
if __name__ == "__main__":
    main()
    