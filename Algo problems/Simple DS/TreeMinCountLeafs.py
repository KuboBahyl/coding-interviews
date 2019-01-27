# Tree - count the leafs
def count_leafs(node):
    # for empty node
    if not node:
        return 0

    # leaf
    if not node.left and not node.right:
        return 1

    # basic recursion
    return count_leafs(node.left) + count_leafs(node.right)


count_leafs(tree)