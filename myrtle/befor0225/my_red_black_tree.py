from enum import Enum
from typing import Any, Optional


class Color(Enum):
    RED = 1
    BLACK = 2


class RedBlackTree:
    def __init__(self, key: int, value: Any):
        self.key = key
        self.color = Color.RED
        self.left: Optional[RedBlackTree] = None
        self.right: Optional[RedBlackTree] = None
        self.value = value
        self.n = 0

    def is_red(self) -> bool:
        return self.color == Color.RED


def rotate_left(node: RedBlackTree) -> RedBlackTree:
    old_right = node.right
    node.right = old_right
    old_right.left = node
    old_right.color = node.color
    node.color = Color.RED
    old_right.n = node.n
    node.n = 1 + node.left.n + node.right.n
    return old_right


def rotate_right(node: RedBlackTree) -> RedBlackTree:
    old_left = node.left
    node.left = old_left.right
    old_left.right = node
    old_left.color = node.color
    node.color = Color.RED
    old_left.n = node.n
    node.n = 1 + node.left.n + node.right.n
    return old_left


def flip_color(node: RedBlackTree):
    node.color = Color.RED
    node.left.color, node.right.color = Color.BLACK, Color.BLACK


def build_tree(key: int, value: Any) -> RedBlackTree:
    root = _put(None, key, value)
    root.color = Color.BLACK
    return root


def _put(node: Optional[RedBlackTree], key: int, value: Any) -> RedBlackTree:
    if not node:
        return RedBlackTree(key, value)

    if key < node.key:
        node.left = _put(node.left, key, value)
    elif key > node.key:
        node.right = _put(node.right, key, value)
    else:
        node.value = value

    if not node.left.is_red() and node.right.is_red():
        node = rotate_left(node)

    if node.left.is_red() and node.left.left and node.left.left.is_red():
        node = rotate_right(node)

    if node.left.is_red() and node.right.is_red():
        flip_color(node)

    node.n = 1 + node.left.n + node.right.n
    return node
