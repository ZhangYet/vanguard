# https://leetcode.com/problems/lru-cache/

# 之前的做法是用 deque 做的，实际的复杂度还是 O(1)
# 尝试自己用链表做

# 答案：https://leetcode.com/problems/lru-cache/discuss/467267/Python3-Video-Explanation-O(1)-solution-(


class DLinkNode:
    def __init__(self, key: int):
        self.prev, self.next = None, None
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = DLinkNode(-1)  # head
        tail = DLinkNode(-1)
        self.head.next = tail
        tail.prev = self.head
        self.tail = tail
        self.data = {}

    def is_full(self) -> bool:
        return len(self.data) >= self.cap

    def insert_into_head(self, node: DLinkNode):
        node.next = self.head.next
        node.prev = self.head.prev
        node.next.prev = node
        self.head.next = node

    def delete_from_tail(self):
        need_delete = self.tail.prev.key
        self.data.pop(need_delete)
        self.tail.prev = self.tail.prev
        self.tail.prev.next = self.tail

    def update_key_chain(self, key: int):
        if key in self.data:  # 只需要找到对应的 node， 然后更新 pos
            cur = self.head.next
            while cur.key != key:
                cur = cur.next

            if cur == self.head.next:
                return  # 如果已经在表头，就不用再交换了

            cur.next.prev = cur.prev
            cur.prev.next = cur.next

            self.insert_into_head(cur)
            return

        new_node = DLinkNode(key)
        self.insert_into_head(new_node)
        if self.is_full():
            self.delete_from_tail()

    def get(self, key: int) -> int:
        res = self.data.get(key, -1)
        if res > -1:
            self.update_key_chain(key)
        return res

    def put(self, key: int, value: int):
        self.update_key_chain(key)
        self.data[key] = value


def test_case():
    s = LRUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    assert s.get(1) == 1
    s.put(3, 3)
    assert s.get(2) == -1
    s.put(4, 4)
    assert s.get(1) == -1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
