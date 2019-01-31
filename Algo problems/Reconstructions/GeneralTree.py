# General tree
class Node(object):
    def __init__(self, value, children = []):
        self.data = value
        self.children = children or []


class Tree(object):
    def __init__(self, root_node=None, children = []):
        self.root = root_node
        self.children = children or []

    def has_root(self):
        if not self.root:
            return print('No root!')

    def print_DFS(self):
        def print_rec(node):
            print(node.data)
            for child in node.children:
                print_rec(child)

        self.has_root()
        print_rec(self.root)

    def print_BFS(self):
        self.has_root()

        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            print(temp_node.data)
            queue.extend(temp_node.children)

    def search_DFS(self, target):
        def search_rec(node):
            if node.data == target:
                return node

            for child in node.children:
                found_node = search_rec(child)
                if found_node:
                    return found_node

            return False

        self.has_root()
        return search_rec(self.root)

    def search_BFS(self, target):
        self.has_root()

        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if temp_node.data == target:
                return temp_node

            queue.extend(temp_node.children)

        return False

    def path_DFS(self, target):
        def path_rec(node, target, path):
            path.append(node.data)
            if node.data == target:
                return True, path

            for child in node.children:
                found, path = path_rec(child, target, path)
                if found:
                    return found, path

            return False, path[:-1]

        self.has_root()
        return path_rec(self.root, target, path=[])

    def path_BFS(self, target):
        self.has_root()

        queue = [self.root]
        path_queue = [[self.root.data]]
        path = []
        while queue:
            temp_node = queue.pop(0)
            path = path_queue.pop(0)

            if temp_node.data == target:
                return True, path

            for child in temp_node.children:
                queue.append(child)
                path_queue.append(path+[child.data])

        return False, path


tree = Tree(Node(1))
root = tree.root
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[1].children = [Node(7)]
root.children[2].children = [Node(8), Node(9)]
root.children[2].children[1].children = [Node(10)]

tree.path_BFS(10)