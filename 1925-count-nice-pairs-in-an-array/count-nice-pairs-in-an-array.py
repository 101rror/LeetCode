import numpy as np
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = []
        count = 0
        mod = 10 ** 9 + 7

        for i in range(n):
            x = str(nums[i])
            x1 = x[::-1]
            y = (nums[i] - int(x1))
            ans.append(y)

        mp = defaultdict(int)

        for i in ans:
            count += mp[i]
            mp[i] += 1

        return int(count % mod)