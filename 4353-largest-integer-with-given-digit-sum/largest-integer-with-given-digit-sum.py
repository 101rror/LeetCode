class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        ans = []
        if 9 * n < s:
            return -1

        while n:
            d = min(9, s)
            ans.append(str(d))
            s -= d
            n -= 1

        return int("".join(ans))
