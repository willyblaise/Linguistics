#!/bin/env python3



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
    
def count_links(head):
        counter = 0
        current = head
        while current.next is not None:
            print(f"Value {counter+1}: {current.data}")
            current = current.next
            counter += 1
        return counter


if __name__ == "__main__":


    nodeA = Node(66)
    nodeB = Node(10)
    nodeC = Node(66)
    nodeD = Node(92)
    nodeE = Node(33)
    nodeF = Node(77)

    nodeA.next = nodeB
    nodeB.next = nodeC
    nodeC.next = nodeD
    nodeD.next = nodeE
    nodeE.next = nodeF


    print(f"The number of links is: {count_links(nodeA)}")

