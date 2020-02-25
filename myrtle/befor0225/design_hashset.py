# https://leetcode.com/problems/design-hashset/
from typing import List


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [None] * 10000

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        index = key % 10000
        if self.data[index]:
            self.data[index].append(key)
            return

        self.data[index] = [key]

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        index = key % 10000
        if not self.data[index]:
            return

        if len(self.data[index]) <= 1:
            self.data[index] = None
            return

        d: List = self.data[index]
        to_del_index = d.index(key)
        self.data[index] = d[:to_del_index] + d[to_del_index + 1 :]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % 10000
        if not self.data[index]:
            return False
        return key in self.data[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


def test_case():
    s = MyHashSet()
    s.add(1)
    s.add(2)
    assert s.contains(1) == True
    assert s.contains(3) == False
