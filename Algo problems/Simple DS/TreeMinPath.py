# N-ary tree: find the min value path and the corresponding path

class Node:
    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None


def get_cheapest_cost(rootNode):
    def search_node(node, path=[]):
        if len(node.children) == 0:
            return node.cost, [node.cost]

        min_child_cost = float('inf')
        min_path = None
        for child_node in node.children:
            child_cost, child_path = search_node(child_node, path)
            if child_cost < min_child_cost:
                min_child_cost = child_cost
                min_path = child_path

        return min_child_cost + node.cost, [node.cost] + min_path

    if not rootNode:
        return

    return search_node(rootNode)


tree = Node(1)
tree.children = [Node(5), Node(3), Node(6)]
tree.children[0].children = [Node(4)]
tree.children[1].children = [Node(2), Node(3)]
tree.children[2].children = [Node(1), Node(5), Node(2)]

get_cheapest_cost(tree)