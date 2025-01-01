class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        mx = 0

        for i in range(1, n):
            left = s[0:i]
            right = s[i:n]

            if left.count("0") > 0 or right.count("1") > 0:
                zero = left.count("0")
                one = right.count("1")

                mx = max(mx, zero + one)

        return mx
