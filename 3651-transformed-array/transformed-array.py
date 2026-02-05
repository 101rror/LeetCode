class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        for i in range(n):
            if nums[i] == 0:
                ans[i] = 0
            else:
                x = (i + nums[i]) % n
                ans[i] = nums[x]

        return ans
