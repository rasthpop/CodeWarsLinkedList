class Node:
    def __init__(self, next=None):
        self.next = next

def loop_size(node):
    slow = node.next
    fast = node.next.next
    
    cur_node = slow
    cur_node_fast = fast
    
    while cur_node != cur_node_fast:
        cur_node = cur_node.next
        cur_node_fast = cur_node_fast.next.next
    
    length = 1
    cur_node = cur_node.next
    
    while cur_node_fast != cur_node:
        cur_node = cur_node.next
        length += 1
    return length
        
    
    
    