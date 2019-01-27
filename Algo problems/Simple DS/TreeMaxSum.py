# Tree - find the max sum path
def best_path(node):
    # empty
    if not node:
        return 0

    # full node
    if node.left and node.right:
        return min(best_path(node.left), best_path(node.right)) + node.val

    elif node.left:
        return best_path(node.left) + node.val

    elif node.right:
        return best_path(node.right) + node.val

    # leaf
    return node.val


best_path(tree)