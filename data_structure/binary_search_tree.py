class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recersive(self, data, root_node):
        if data['id'] < root_node.data['id']:
            if root_node.left is None:
                root_node.left = Node(data)
            else:
                self._insert_recersive(data, root_node.left)
        elif data['id'] > root_node.data['id']:
            if root_node.right is None:
                root_node.right = Node(data)
            else:
                self._insert_recersive(data, root_node.right)

        else:
            return
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recersive(data, self.root)

    def _search_recursive(self,data_id, node):
        # if node.left == None and node.right == None:
        #     return False

        if data_id == node.data['id']:
            return node.data

        if data_id < node.data['id'] and node.left is not None:
            if data_id == node.left.data['id']:
                return node.left.data 
            return self._search_recursive(data_id, node.left)
           
        if data_id > node.data['id'] and node.right is not None:
            if data_id == node.right.data['id']:
                return node.right.data 
            return self._search_recursive(data_id, node.right)
        return False
        

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False

        return self._search_recursive(blog_post_id, self.root)

    
