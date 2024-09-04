class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        ans = ''

        for i in range(0, n, k):
            substr = s[i : i + k]
            hsum = 0

            for char in substr:
                hsum += alpha.index(char)

            hsum %= 26

            ans += alpha[hsum]

        return ans

