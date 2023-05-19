class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        n1 = len(word1)
        n2 = len(word2)
        n = max(n1, n2)

        for i in range(n):
            if (n1 > i):
                ans += word1[i]
            if (n2 > i):
                ans += word2[i]
        return ans