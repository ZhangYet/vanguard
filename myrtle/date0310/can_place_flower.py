# https://leetcode.com/problems/can-place-flowers/
# 先用普通的思路，判断每个0是否合法，然后将对应的位置改成1，然后n减一，把n减为0之后就返回True
# 但是会有很多边界条件导致我们代码很臃肿
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        tmp = [0] + flowerbed + [0]
        index = 1
        while index < len(tmp) - 1:
            if tmp[index-1] == 0 and tmp[index] == 0 and tmp[index+1] == 0:
                n -= 1
                if n <= 0:
                    return True
                index += 1
            index += 1
        return n <= 0
                
