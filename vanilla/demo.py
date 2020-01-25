from graphviz import Digraph

class Node:

    def __init__(self, value: int, name: str):
        self.value = value
        self.left, self.right = None, None
        self.name = name


def test_case():
    node0 = Node(0, 'root')
    node1 = Node(1, 'left')
    node2 = Node(2, 'right')
    node0.left = node1
    node0.right = node2

    dot = Digraph(comment='Demo')
    dot.node(node0.name)
    dot.node(node1.name)
    dot.node(node2.name)
    dot.edge(node0.name, node1.name)
    dot.edge(node0.name, node2.name)
    dot.render('demo.png')