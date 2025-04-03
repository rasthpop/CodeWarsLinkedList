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
    if head is None or head.next is None:
        return head

    reversed_list = reverse(head.next)
    head.next.next = head
    head.next = None

    return reversed_list

m = build_one_two_three()

l = reverse(m)
