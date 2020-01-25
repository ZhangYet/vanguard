# implement heap using list
from typing import List


# 其实就是层遍历啊
class ListHeap:

    def __init__(self, nums: List[int]):
        self.heap: List[int] = nums
        self._build_heap()

    def _left_child(self, i: int) -> int:
        return 2 * i + 1

    def _right_child(self, i: int) -> int:
        return 2 * i + 2

    def _heapify(self, i):
        print(f'heapify {i}')
        l = self._left_child(i)
        r = self._right_child(i)

        heap_size = len(self.heap)
        largest = l if l < heap_size and self.heap[l] > self.heap[i] else i

        largest = r if r < heap_size and self.heap[r] > self.heap[largest] else largest

        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self._heapify(largest)

        return

    def _build_heap(self):
        heap_size = len(self.heap)
        for i in range(heap_size // 2, -1, -1):
            self._heapify(i)



def test_case():
    nums: List[int] = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    h = ListHeap(nums)
    print(h.heap)
