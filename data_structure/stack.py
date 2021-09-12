class Node:
    def __init__(self, data, next_):
        self.data = data
        self.next_ = next_


class Stack:
    def __init__(self):
        self.top = None

    def peek(self):
        return self.top

    def push(self, data):
        next_node = self.top
        new_node = Node(data, next_node)
        self.top = new_node

    def pop(self):
        if self.top is None:
            return False

        remove = self.top
        self.top = self.top.next_
        return remove
