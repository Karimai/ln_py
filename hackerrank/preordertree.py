class Node:
    def __init__(self, info = None, level=None, right= None, left=None):
        self.info = info
        self.level = level
        self.left = left
        self.right = right


def preOrder(node):
    if node:
        print(node.info)
        if node.left:
            preOrder(node.left)
        if node.right:
            preOrder(node.right)


def test_preOrder():
    nodes = Node(1, 1)
    nodes.right = Node(2, 1)
    nodes.right.right = Node(5, 3)
    nodes.right.right.left = Node(3, 4)
    nodes.right.right.right = Node(6, 4)
    nodes.right.right.left.right = Node(4, 5)
    preOrder(nodes)
