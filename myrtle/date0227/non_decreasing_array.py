# https://leetcode.com/problems/non-decreasing-array/
# 一眼看起来很复杂，但其实记录一下遇到的非升的次数就行了
# 啊，但是也没有那么简单，比如说 [3,4,2,3]
# 这样的话两两比较不能刻画整个数组的升降情况
# 临时改变一下数据的数值其实也不行
# 总的来说，就是要处理锯齿状的数组比较困难，比如 [1, 2, 3, 4, 1, 2, 1, 2] 这种
# 我们可以找 gap 就是比后面一个数大的数，然后比较 gap 后面的数跟 gap 前面的数的大小
# 然后要处理 gap 在位置 1 的情况贼烦

# trival 的解很简单：
# 如果找到一个非升的位置，把这个位置对应的数去掉，如果剩下的数组是非降的，那么 ok

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True

        if len(nums) == 3:
            return not (nums[0] > nums[1] and nums[1] > nums[2])

        def is_not_decreasing(nums: List[int]) -> bool:
            if not nums or len(nums) == 1:
                return True

            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False

            return True

        nums1 = nums[:]
        nums2 = nums[:]
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                nums1[i] = nums[i - 1]
                nums2[i - 1] = nums[i]
                break

        return is_not_decreasing(nums1) or is_not_decreasing(nums2)


def test_case():
    s = Solution()
    assert s.checkPossibility([4, 2, 3]) == True
    assert s.checkPossibility([4, 2, 1]) == False
    assert s.checkPossibility([3, 4, 3, 2]) == False
    assert s.checkPossibility([-1, 4, 2, 3]) == True
