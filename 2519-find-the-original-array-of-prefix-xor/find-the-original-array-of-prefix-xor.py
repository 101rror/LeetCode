class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        n = len(pref)

        for i in range(1, n):
            x = (pref[i - 1] ^ pref[i])
            ans.append(x)

        return ans