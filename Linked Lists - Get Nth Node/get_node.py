"""get nth node"""

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def get_nth(node, index):
    if node == None:
        raise ValueError

    if index < 0:
        raise IndexError
    i = 0
    cur_node = node
    if index > 0:
        while True:
            cur_node = cur_node.next
            i += 1
            if i == index:
                break
            if cur_node.next == None:
                raise IndexError

    return cur_node
