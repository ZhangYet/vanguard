class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if B == A:
            return True

        for i in range(len(B)):
            tmp = B[i:] + B[:i]
            if tmp == A:
                return True

        return False
