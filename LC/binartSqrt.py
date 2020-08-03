class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        lf, rt, res = 1, x, x
        while lf <= rt:
            mid = (lf + rt) // 2
            tmp = mid * mid
            if tmp == x:
                return int(mid)
            elif tmp < x:
                lf = mid + 1
                res = mid
            else:
                rt = mid - 1

        return int(res)