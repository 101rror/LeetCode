class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        n = len(nums)
        ans = n

        for i in range(n):
            if nums[i] == target:
                ans = min(ans, abs(i - start))

        return ans
