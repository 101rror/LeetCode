class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        for i in order:
            if i in s:
                ans += (i * s.count(i))
                s = s.replace(i, '')

        return ans + s
