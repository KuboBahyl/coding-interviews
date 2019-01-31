class Node(object):
    def __init__(self, value, left_node=None, right_node=None):
        self.data = value
        self.left = left_node
        self.right = right_node


class Tree(object):
    def __init__(self, root_node):
        self.root = root_node

    def print_BFS(self):
        if not self.root:
            return

        temp_node = self.root
        queue = [temp_node]
        while queue:
            temp_node = queue.pop(0)
            print(temp_node.data)
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)

    def insert_new_value(self, new_value):
        def insert_rec(node, new_value):
            if new_value == node.data:
                return print("Value {} already in search tree!".format(new_value))

            if new_value > node.data:
                if node.right:
                    insert_rec(node.right, new_value)
                else:
                    node.right = Node(new_value)
                    return
            else:
                if node.left:
                    insert_rec(node.left, new_value)
                else:
                    node.left = Node(new_value)
                    return

        return insert_rec(self.root, new_value)


tree = Tree(Node(5))
root = tree.root
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.right = Node(10)

tree.insert_new_value(6)
tree.insert_new_value(10)
tree.insert_new_value(11)
tree.print_BFS()