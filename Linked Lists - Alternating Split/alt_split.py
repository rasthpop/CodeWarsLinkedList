class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    i = 2
    first_ll = Node(head.data)
    cur_first = first_ll
    second_ll = None
    cur_second = second_ll

    cur_node = head.next
    while True:
        if cur_node is None:
            break

        if i % 2 != 0:
            cur_first.next = Node(cur_node.data)
            cur_first = cur_first.next
        else:
            if second_ll is None:
                second_ll = Node(cur_node.data)
                cur_second = second_ll
            else:
                cur_second.next = Node(cur_node.data)
                cur_second = cur_second.next
        if head is None or head.next is None:
            break

        cur_node = cur_node.next

        i += 1

    return Context(first_ll , second_ll)
