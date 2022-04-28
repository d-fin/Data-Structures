'''
Author: David Finley 
BST - Creating a binary tree then searching that tree. 
'''
from Node import Node 

def main():
    #nums = [22, 20, 10, 4, 17, 18, 102, 99, 66, 2]
    nums = []
    q = True
    tree = None 
    print("\n\nLets create a Binary Search Tree!")
    while q == True:
        try: 
            x = int(input("Please input a positive number or -1 to quit: "))
            if x == -1:
                q = False 
                break 
            nums.append(x)
        except:
            print("Please only enter integers.")
    
    for i in range(len(nums)):
        if i == 0:
            tree = Node(nums[i])
        else:
            tree = insert(tree, nums[i])
    
    z = True 
    print("\n\nSearch - below are the values in the tree")
    print(nums)
    while z == True:
        key = int(input("\nEnter the node you would like to search for or -1 to quit: "))
        if key == -1: 
            print("Goodbye :)")
            z = False 
            break
        # returns list [parent, left, right] -> searched node will be one of the children
        nodes = getParent(tree, key, -1)
        if nodes == -1:
            print("That value is not in the tree. Please re-enter")
        else:
            printNodes(nodes, key)
        

def printNodes(nodes, key):
    parent, lc, rc = 'None', 'None', 'None' 
    
    if len(nodes) == 1:
        print(f'\n{key} is the root node in our binary tree!')
    else:
        if nodes[0] != None: parent = str(nodes[0].val)
        if nodes[1] != None: lc = str(nodes[1].val)
        if nodes[2] != None: rc = str(nodes[2].val) 

        x = ' '
        print(f'\n{x * (10 - len(parent))}{parent}')
        print(f'{x * ((10 - len(parent)) - 1)}/', end = "")
        print(f' \ ')
        print(f'{x * ((10 - len(lc)) - 2)}{lc}   {rc}')
        print(f'\nThe node {key} has been found, also displayed is its parent node and its position under the parent\n')

def getParent(root, x, parent):
    if root == None:
        return -1 
    else:
        if root.val == x:
            if parent == -1: return [root]
            else: return [parent, parent.left, parent.right] 
        elif root.val > x:
            return getParent(root.left, x, root)
        elif root.val < x:
            return getParent(root.right, x, root)
        else:
            return -1

def insert(root, x):
    if root is None:
        return Node(x)
    else:
        if root.val == x:
            return root
        elif x > root.val:
            root.right = insert(root.right, x)
        elif x < root.val:
            root.left = insert(root.left, x)
    return root

if __name__ == '__main__':
    main()