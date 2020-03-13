# https://leetcode.com/problems/lru-cache/
# 直接在 dict 里面保存 double link list 的节点


class LinkedNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev, self.next = None, None

    def output(self):
        res = []
        cur = self
        while cur:
            res.append((cur.key, cur.val))
            cur = cur.next
        return res


def debug(f):
    def _(*args, **kwargs):
        self = args[0]
        print(f"before {f.__name__}: {self.head.output()}")
        res = f(*args, **kwargs)
        print(f"after {f.__name__}: {self.head.output()}")
        return res

    return _


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        head, tail = LinkedNode(-1, -1), LinkedNode(-1, -1)
        self.head, self.tail = head, tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}

    def is_full(self) -> bool:
        return len(self.data) >= self.capacity

    def delete_from_tail(self):
        to_delete = self.tail.prev
        self.data.pop(to_delete.key)
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

    def insert_into_head(self, node: LinkedNode):
        # 断开原来的关系
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        # 插到头里
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        res = self.data.get(key, None)
        if not res:
            return -1

        self.insert_into_head(res)
        return res.val

    def put(self, key: int, val: int):
        if key in self.data:
            self.get(key)
            self.data[key].val = val
            return

        if self.is_full():
            self.delete_from_tail()

        new_node = LinkedNode(key, val)
        self.insert_into_head(new_node)
        self.data[key] = new_node


# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
def test_case():
    s = LRUCache(2)
    s.put(2, 1)
    s.put(1, 1)
    s.put(2, 3)
    s.put(4, 1)
    assert s.get(1) == -1
    assert s.get(2) == 3
