from gvanim import Animation, render, gif

class Node:

    def __init__(self, value: int, name: str):
        self.value = value
        self.left, self.right = None, None
        self.name = name


def preorder(root: Node, ga: Animation):
    if not root:
        return

    ga.highlight_node(root.name)

    if root.left:
        ga.next_step()
        ga.highlight_edge(root.name, root.left.name)
        ga.next_step()

    preorder(root.left, ga)

    if root.right:
        ga.next_step()
        ga.highlight_edge(root.name, root.right.name)
        ga.next_step()

    preorder(root.right, ga)


def test_case():
    node0 = Node(0, 'root')
    node1 = Node(1, 'left')
    node2 = Node(2, 'right')
    node3 = Node(3, 'll-child')
    node4 = Node(4, 'lr-child')
    node0.left = node1
    node0.right = node2
    node1.left = node3
    node1.right = node4

    ga = Animation()
    ga.add_edge(node0.name, node1.name)
    ga.add_edge(node0.name, node2.name)
    ga.add_edge(node1.name, node3.name)
    ga.add_edge(node1.name, node4.name)
    ga.next_step()

    preorder(node0, ga)

    graphs = ga.graphs()
    for g in graphs:
        print(g)

    output = render(graphs, 'demo', 'png')
    gif(output, 'demo', 50)







