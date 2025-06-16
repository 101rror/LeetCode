class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxDif = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                dif = nums[j] - nums[i]
                if dif > maxDif:
                    maxDif = dif

        return maxDif if maxDif > 0 else -1
