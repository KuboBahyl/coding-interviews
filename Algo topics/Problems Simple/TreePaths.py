# Tree - print the paths
def print_tree_paths(node):
    def search_next_path(node, path=[]):
        path.append(node.val)

        if not node.left and not node.right:
            print(path)
            return path[:-1]

        if node.left:
            path = search_next_path(node.left, path)
        if node.right:
            path = search_next_path(node.right, path)

        return path[:-1]

    if not node:
        return

    path = []
    search_next_path(node)


print_tree_paths(tree)