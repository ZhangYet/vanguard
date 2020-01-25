# implement heap using list
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


def heap_sort(nums: List[int]) -> List[int]:
    h = ListHeap(nums)
    res: List[int] = [0] * len(nums)

    for i in range(len(nums) - 1, 0, -1):
        h.heap[0], h.heap[-1] = h.heap[-1], h.heap[0]
        tmp = h.heap.pop()
        res[-(i + 1)] = tmp
        h.heapify(0)

    return res


def test_case():
    nums: List[int] = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = ListHeap(nums)
    print(h.heap)
