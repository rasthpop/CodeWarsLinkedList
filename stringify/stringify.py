"""Convert a linked list to a string"""

class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if not node:
        return "None"
    cur_node = node
    node_data = [str(cur_node.data)]
    while cur_node.next:
        cur_node = cur_node.next
        node_data.append(str(cur_node.data))

    return " -> ".join(node_data) + " -> None"
