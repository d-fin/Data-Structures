class StackParenthesisChecker():
    #constructor for stack parentheses checker
    def __init__(self):
        return 

    #checks if parentheses are balanced 
    def isBalanced(self, str):
        __queue1 = []
        __queue2 = []
        length = len(str)
        if str[0] == ")" or str[length - 1] == "(":
            return False 
        
        for i in range(0, len(str)):
            if str[i] == "(":
                __queue1.append(str[i])
            elif str[i] == ")":
                __queue2.append(str[i])
            if len(__queue2) > len(__queue1):
                return False 
        
        if len(__queue1) == len(__queue2):
            return True 
        else:
            return False 