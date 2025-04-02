class Node(object):
    def __init__(self, data=None):
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


def reverse(head):
    if head is None:
        return None

    if head.next is None:
        return head

    re
   

    return head

m = build_one_two_three()

reverse(m)
