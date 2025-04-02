#  For your information:


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    insertion_node = Node(data)
    cur_node = head

    if head is None:
        return insertion_node

    while True:
        if cur_node is None:
            break

        if cur_node.data > data:
            insertion_node.next = cur_node
            return insertion_node

        if cur_node.next is None or cur_node.next.data > data:
            insertion_node.next = cur_node.next
            cur_node.next = insertion_node
            break
        cur_node = cur_node.next
    return head


