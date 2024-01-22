class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tsum = sum(nums)
        ans = []
        nums.sort()

        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                ans.append(nums[i - 1])

        x = ((n * (n + 1)) // 2) - (tsum - ans[0])
        ans.append(x)

        return ans
