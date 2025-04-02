"""Linked Lists - Push & BuildOneTwoThree"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    if head:
        new_node = Node(data)
        new_node.next = head
        return new_node
    return Node(data)

def build_one_two_three():
    ll = push(push(push(None, 3), 2), 1)
    return ll
