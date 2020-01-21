from ctypes import c_float, c_int32, cast, byref, POINTER

class Solution:
    def mySqrt(self, x: int) -> int:

        def _q_sqrt(num):
            th = 1.5
            x = 0.5 * num
            y = c_float(num)

            i = cast(byref(y), POINTER(c_int32)).contents.value
            i = c_int32(0x5f3759df - (i >> 1))
            y = cast(byref(i), POINTER(c_float)).contents.value
            return y * (th - (x * y * y))

        return int(round(_q_sqrt(x) * x, 2))


def test_case(x: int) -> int:
    s = Solution()
    return s.mySqrt(x)