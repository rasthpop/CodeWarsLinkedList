"""remove duplicates"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    
    memory = set()
    cur_node = head
    memory.add(cur_node.data)

    while True:
        if cur_node is None or cur_node.next is None:
            break

        if cur_node.next.data in memory:
            if cur_node.next.next is not None:
                cur_node.next = cur_node.next.next
            else:
                cur_node.next = None
        else:
            cur_node = cur_node.next
            memory.add(cur_node.data)

    return head