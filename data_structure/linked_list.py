class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        list_ = []
        if self.head is None:
            return list_
        current = self.head
        while current:
            list_.append(current.data)
            current = current.next_
        
        return list_


    def print_(self):
        linkedListString = ''
        current = self.head
        if current is None:
            print(None)
        else:
            while current:
                linkedListString += f'{current.data} -> '
                current = current.next_
        linkedListString += " None"
        return linkedListString

    def insert_start(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
        if self.head is None:
            self.insert_start(data)
            return
        # if self.last_node is None:
        #     current = self.head
        #     while current.next_:
        #         current = current.next_

            # current.next_ = Node(data, None)
            # self.last_node = current.next_
            
        self.last_node.next_ = Node(data, None)
        self.last_node = self.last_node.next_

    def get_user_by_id(self, user_id):
        current = self.head
        while current:
            if current.data['id'] is int(user_id):
                return current.data
            current = current.next_
        return None

ll = LinkedList()
ll.insert_end("Start1")
ll.insert_end("Start2")
ll.insert_end("Start3")
ll.insert_end("Start4")
ll.insert_end("Start5")
ll.insert_end("Start6")
ll.insert_end("Start7")
ll.insert_end("end")
print(ll.print_())

# if __name__ == "__main__":
#     LinkedList()
