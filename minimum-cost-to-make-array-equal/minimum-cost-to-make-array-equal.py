class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def fcost(n):
            total = 0
            for i in range(len(cost)):
                total += (abs(n - nums[i]) * cost[i])
            return total
        
        first = min(nums)
        last = max(nums)
        while (first < last):
            mid = (first + last) // 2

            if fcost(mid) < fcost(mid+1):
                last = mid
            else:
                first = mid + 1

        return fcost(first)