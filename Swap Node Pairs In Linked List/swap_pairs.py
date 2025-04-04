class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    cur_node = head
    cur_node_next = head.next

    cur_node.next = swap_pairs(cur_node_next.next)
    cur_node_next.next = cur_node

    return cur_node_next
