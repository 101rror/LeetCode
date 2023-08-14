class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)
        mx = -1

        for i in range(n):
            for j in range(i + 1, n):
                if(max(str(nums[i])) == max(str(nums[j]))):
                    mx = max(mx, nums[i] + nums[j])

        return mx