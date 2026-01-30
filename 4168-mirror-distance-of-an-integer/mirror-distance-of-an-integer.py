class Solution:
    def mirrorDistance(self, n: int) -> int:
        r, x = 0, n

        while x > 0:
            r = r * 10 + x % 10
            x //= 10

        return abs(n - r)
