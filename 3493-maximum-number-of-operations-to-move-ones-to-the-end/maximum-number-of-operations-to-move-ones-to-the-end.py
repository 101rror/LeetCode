class Solution:
    def maxOperations(self, s: str) -> int:
        one, ans = 0, 0

        for i, c in enumerate(s):
            if c == "1":
                one += 1
            elif s[i - 1] == "1":
                ans += one

        return ans
