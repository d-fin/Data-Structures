'''
Author: David Finley 
Priority queue using a linked list:
Time complexity = O(n)
Better implementation would be to use a minheap.
'''
from PriorityQueue import PriorityQueue 

def main():
    id = [50, 100, 125, 56, 73, 58, 1002, 98, 200, 750]
    priority = [1, 3, 5, 2, 9, 7, 8, 4, 6, 10]

    data = {50 : "Jeff", 100 : "Steve", 125 : "David", 56: "Erin", 73 : "Mike", 58: "Maggie", 1002 : "Mary", 98 : "Rachel",
             200 : "Stephanie", 750 : "Gerry"}

    pq = PriorityQueue()
    for i in range(len(id)):
        pq.push(id[i], priority[i])

    x = ' '
    print(f'Priority{x * 3}Value{x * 5}Name')
    print("-" * 30)
    while pq.isEmpty() == False:
        p = str(pq.front.priority)
        id = pq.front.value

        for key in data:
            if key == id:
                name = data[key]

        print(f'{p:<8} : {str(id):<7} : {name:<5}')
        pq.pop()

if __name__ == '__main__':
    main()