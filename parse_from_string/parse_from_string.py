"""Parse a linked list from a string}"""

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    if s == "None":
        return None

    curr_node = None
    nodes = [int(el) if el.isnumeric() else None for el in s.split(" -> ")][:-1]
    nodes.reverse()

    linked_list = Node(nodes.pop)
    if nodes:
        linked_list.next = Node(nodes.pop())
        curr_node = linked_list.next

    while nodes:
        curr_node.next = Node(nodes.pop())
        curr_node = curr_node.next


    return linked_list
