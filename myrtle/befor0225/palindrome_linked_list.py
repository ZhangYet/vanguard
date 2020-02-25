# https://leetcode.com/problems/palindrome-linked-list/

# 最简单的方法当然是把这条链倒转，然后比较新链跟旧链

# 但是慢，用 stack 的话，最大的问题是对称性的问题，局部对称性推不出整体对称性。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return None

# 看了答案，结果还是要 reverse 啊