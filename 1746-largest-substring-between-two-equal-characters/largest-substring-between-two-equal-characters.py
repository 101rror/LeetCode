class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        count = -1

        for i in range(n):
            for j in range(i + 1, n):
                if(s[i] == s[j]):
                    count = max(count, j - i - 1)

        return count 
            