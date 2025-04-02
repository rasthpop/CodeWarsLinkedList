class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if not source:
        raise ValueError
    first_node = Node(source.data)
    source = source.next
    first_node.next = dest
    dest = first_node
    return Context(source, dest)
