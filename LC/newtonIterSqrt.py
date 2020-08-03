def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        r = x // 2
        while r * r > x:
            r = (r + x // r) // 2
        return int(r)