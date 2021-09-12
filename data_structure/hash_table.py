class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value
    
    def add_key_value(self, key, value):
        hashed_value = self.hash(key)
        if self.hash_table[hashed_value] is None:
            self.hash_table[hashed_value] = Node(Data(key ,value), None)
        else:
            node = self.hash_table[hashed_value]
            while node.next_:
                node = node.next_
            node.next_ = Node(Data(key, value), None)

    def get_value(self, key):
        hash_val = self.hash(key)
        if self.hash_table[hash_val] is not None:
            node = self.hash_table[hash_val]
            if node.next_ is None:
                return node.data.value

            while node.next_:
                if key == node.data.key:
                    return node.data.value
                node = node.next_
            if key == node.data.key:
                return node.data.value
        return None

    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_:
                    while node.next_:
                        llist_string += f"{str(node.data.key)} : {str(node.data.value)} -->"
                        node = node.next_
                    llist_string += f"{str(node.data.key)} : {str(node.data.value)} --> None"
                    print(f"    [{i}] {llist_string}" )
                else:
                    print(f"    [{i}] {node.data.key} : {node.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")


# tb = HashTable(5)
# tb.add_key_value("harsh", "madhesia")
# tb.add_key_value("harsh", "madhesia")
# tb.add_key_value("harsh", "madhesia")
# tb.print_table()
