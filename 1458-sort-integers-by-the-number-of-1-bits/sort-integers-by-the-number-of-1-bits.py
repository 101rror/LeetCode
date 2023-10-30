from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lst = defaultdict(list)

        for i in arr:
            lst[bin(i).count('1')].append(i)

        ans = []

        for k in sorted(lst.keys()):
            for i in sorted(lst[k]):
                ans.append(i)
        return ans


        