class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        alpha = 'abcdefghijklmnopqrstuvwxyza'
        i, j = 0, 0
        n, m = len(str1), len(str2)

        while i < n and j < m:
            if str1[i] == str2[j]:
                j += 1
            elif alpha[(alpha.index(str1[i]) + 1) % 26] == str2[j]:
                j += 1
            i += 1

        return j == m