class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        st = collections.Counter(s)

        for i in range(n):
            if(st[s[i]] == 1):
                return i

        return -1