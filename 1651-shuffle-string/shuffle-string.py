class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        ans = [''] * n
        j = 0

        for i in indices:
            ans[i] += s[j]
            j += 1 

        return "".join(ans)