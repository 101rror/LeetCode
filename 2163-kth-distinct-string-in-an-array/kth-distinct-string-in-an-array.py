from collections import defaultdict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = []
        map = defaultdict(int)

        for i in arr:
            map[i] += 1

        for i, j in map.items():
            if j == 1:
                ans.append(i)

        return ans[k - 1] if len(ans) >= k else ""