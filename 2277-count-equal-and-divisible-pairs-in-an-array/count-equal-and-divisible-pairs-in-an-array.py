from collections import defaultdict


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        mp = defaultdict(lambda: defaultdict(int))
        ans = 0

        for i, num in enumerate(nums):
            mi = i % k
            if num in mp:
                for mj, count in mp[num].items():
                    if (mi * mj) % k == 0:
                        ans += count
            mp[num][mi] += 1

        return ans
