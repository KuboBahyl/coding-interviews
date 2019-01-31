# Tree - calculate the min depth of a tree
def min_depth(node):
    # escape - only for None input
    if not node:
        return 0

    # case = leaf
    if not node.left and not node.right:
        return 1

    # case =
    if not node.left:
        return min_depth(node.right) + 1

    if not node.right:
        return min_depth(node.left) + 1

    # basic recursion - always choosing the lower value
    return min(min_depth(node.left), min_depth(node.right)) + 1


min_depth(tree)