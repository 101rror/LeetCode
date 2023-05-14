"""
import math

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        ln = len(nums)
        ans = []
        res = []
        a = []
        b = []
        tsum = 0

        for i in range(0, ln // 2):
            a.append(nums[i])
        for i in range(ln // 2, ln):
            b.append(nums[i])

        if(ln == 2):
            return math.gcd(nums[0], nums[1])
        else:
            for i in range(0, ln // 2):
                x = a[i]
                y = b[i]

                gd = math.gcd(x, y)
                ans.append(gd)

            ct = 1
            for j in range(0, len(ans)):
                m = (ct * ans[j])
                res.append(m)
                ct += 1
            result = sum(res)
        return result    
"""

from math import gcd
from functools import lru_cache

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(maxsize = None)

        def dfs(a, x, y, i):
            new_a = a[:x] + a[x+1:y] + a[y+1:]
            n = len(new_a)
            maxScore = 0
            
            for j in range(n):
                for k in range(j+1, n):
                    maxScore = max(maxScore, dfs(new_a, j, k, i+1))

            return i * gcd(a[x], a[y]) + maxScore
        
        nums.sort()
        nums = tuple(nums)
        n = len(nums)
        maxScore = 0
        
        for j in range(n):
            for k in range(j+1, n):
                maxScore = max(maxScore, dfs(nums, j, k, 1))
                
        return maxScore