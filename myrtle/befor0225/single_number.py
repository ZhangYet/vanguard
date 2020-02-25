from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        back_up = []
        while nums:
            tmp = nums.pop()
            if tmp not in nums and tmp not in back_up:
                return tmp
            back_up.append(tmp)



def test_case(l: List[int]) -> int:
    s = Solution()
    return s.singleNumber(l)