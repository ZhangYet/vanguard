# https://leetcode.com/problems/lfu-cache/
# 这个答案是错的
from collections import OrderedDict
from collections import defaultdict
from typing import Tuple, Dict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count_dict = defaultdict(OrderedDict)
        self.min_count = 1
        self.key_dict: Dict[Tuple[int]] = {}

    def _evictLFUKey(self) -> None:
        key_to_evict, datum_to_evict = self.count_dict[self.min_count].popitem(
            last=False
        )
        del self.key_dict[key_to_evict]

    def _updateCacheWithUsage(
        self, key: int, new_datum_node: Tuple[int], old_datum_node: Tuple[int] = None
    ) -> None:
        # update key val store
        self.key_dict[key] = new_datum_node

        if old_datum_node:  # if we are just replacing a preexisting key's val
            del self.count_dict[old_datum_node[1]][key]
            if not self.count_dict[old_datum_node[1]]:
                del self.count_dict[old_datum_node[1]]

        if not self.count_dict[
            self.min_count
        ]:  # if there is no data for the old min_count key, then the new min_count has to be the new datum's count
            self.min_count = new_datum_node[1]

        else:  # we are inserting a new node, meaning our min_count will be 1
            self.min_count = 1

        self.count_dict[new_datum_node[1]][key] = new_datum_node

    def get(self, key: int) -> int:
        # getting an element always puts it at the end of the LRU (of the new count key)
        if not key in self.key_dict:
            return -1

        old_datum = self.key_dict[key]
        new_datum = (old_datum[0], old_datum[1] + 1)
        self._updateCacheWithUsage(key, new_datum, old_datum)

        return new_datum[0]

    def put(self, key: int, value: int) -> None:
        if not self.capacity:
            return

        if key not in self.key_dict:  # if we are insering a new key
            new_datum = (value, 1)
            if len(self.key_dict) == self.capacity:
                self._evictLFUKey()
            self._updateCacheWithUsage(key, new_datum)
        else:  # else we are updating an preexisting key
            old_datum = self.key_dict[key]
            new_datum = (value, old_datum.count + 1)
            self._updateCacheWithUsage(key, new_datum, old_datum)


def test_case():
    s = LFUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    s.get(1)
    s.put(3, 3)
    s.get(2)
    s.get(3)
    s.put(4, 4)
    s.get(1)
    s.get(3)
    s.get(4)
