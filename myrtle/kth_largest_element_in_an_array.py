# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List


class ListHeap:
    def __init__(self, nums: List[int]):
        self.heap: List[int] = nums
        self._build_heap()

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    def heapify(self, i):
        l = self._left_child(i)
        r = self._right_child(i)

        heap_size = len(self.heap)
        largest = l if l < heap_size and self.heap[l] > self.heap[i] else i

        largest = r if r < heap_size and self.heap[r] > self.heap[largest] else largest

        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self.heapify(largest)

        return

    def _build_heap(self):
        heap_size = len(self.heap)
        for i in range(heap_size // 2, -1, -1):
            self.heapify(i)

    def maximum(self) -> int:
        return self.heap[0]

    def extract_max(self) -> int:
        if not self.heap:
            raise Exception("heap underflow")

        max, self.heap[0] = self.heap[0], self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return max

    def yield_max(self):
        while self.heap:
            yield self.extract_max()

    def _parent(self, i):
        return (i - 1) // 2

    def heap_increase_key(self, i: int, key: int):
        if key < self.heap[i]:
            raise Exception("new key is smaller than current key")

        self.heap[i] = key
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self.heap[self._parent(i)], self.heap[i] = (
                self.heap[i],
                self.heap[self._parent(i)],
            )
            i = self._parent(i)

        return

    def insert(self, key: int):
        self.heap.append(key)
        self.heap_increase_key(len(self.heap) - 1, key)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = ListHeap(nums)
        res = 0
        for _ in range(k):
            res = heap.extract_max()

        return res


def test_case():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    s = Solution()
    assert s.findKthLargest(nums, k) == 5
