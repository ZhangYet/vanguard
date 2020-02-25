from typing import List, Tuple


class BNode:
    def __init__(self):
        self.n: int = 0
        self.keys: List[int] = []
        self.is_leaf: bool = True
        self.children: List[BNode] = []


def b_tree_search(r: BNode, key: int) -> Tuple[BNode, int]:
    i = 0
    while i < r.n and key > r.keys[i]:
        i += 1

    if i < r.n and key == r.keys[i]:
        return r, i

    if r.is_leaf:
        return ()

    return b_tree_search(r.children[i], key)


DEGREE = 4


def b_tree_split_child(root: BNode, i: int, child: BNode):
    if child.n < 2 * DEGREE - 1:
        raise Exception("why do you split if it is not full")

    new_child = BNode()
    new_child.is_leaf = child.is_leaf
    s = child.keys[DEGREE]
    child.n, new_child.n = DEGREE - 1, DEGREE - 1
    child.keys, new_child.keys = child.keys[:DEGREE], child.keys[(DEGREE + 1) :]
    child.children, new_child.children = (
        child.children[:DEGREE],
        child.children[(DEGREE + 1) :],
    )

    root.keys.insert(i, s)
    root.children.insert(i, new_child)
    root.n += 1


def b_tree_insert_notfull(root: BNode, key: int):
    i = root.n - 1
    if root.is_leaf:
        while i >= 0 and key < root.keys[i]:
            i -= 1
        root.keys.insert(i, key)
        root.n += 1
        return

    while i >= 0 and key < root.keys[i]:
        i -= 1

    if root.children[i].n == 2 * DEGREE - 1:
        b_tree_split_child(root, i, root.children[i])
        if key > root.keys[i]:
            i += 1
    return b_tree_split_child(root.children[i], key)


def b_tree_insert(root: BNode, key: int):
    if root.n == 2 * DEGREE - 1:
        new_root = BNode()
        new_root.is_leaf = False
        new_root.n = 0
        new_root.children[0] = root
        b_tree_split_child(new_root, 1, root)
        b_tree_insert_notfull(new_root, key)
    return b_tree_insert_notfull(root, key)
