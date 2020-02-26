# https://leetcode.com/problems/sum-of-two-integers/
# 这就纯粹是位运算的知识了
# 这个难题就在于进位和正负
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
            print(f"b after shifting: {b}")
        return a


# shit
# int getSum(int a, int b){
#     while (b != 0) {
#         int carry = a & b;
#         a = a ^ b;
#         b = (unsigned int) carry << 1;
#     }
#     return a;
# }
