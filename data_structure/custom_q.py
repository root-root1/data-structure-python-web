class Node:
    def __init__(self, data, next_):
        self.data = data
        self.next_ = next_
    

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        if self.head == None and self.tail == None:
            self.head = self.tail = Node(data, None)
            return 
        
        self.tail.next_ = Node(data, None)
        self.tail = self.tail.next_

    def dequeue(self):
        if self.head is None:
            return None

        remove = self.head
        self.head = self.head.next_
        if self.head is None:
            self.tail = None
        return remove


if __name__ == '__main__':
    Queue()
