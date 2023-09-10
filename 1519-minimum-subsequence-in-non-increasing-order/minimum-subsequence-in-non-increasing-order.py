class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        tsum = sum(nums)
        nums = sorted(nums, reverse = True)
        n = len(nums)
        ans = []

        for i in range(n):
            if(sum(ans) > tsum):
                break
            else:
                ans.append(nums[i])
                tsum -= nums[i]

        return ans
        