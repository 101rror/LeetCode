class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0] * n
        pos, neg = 0, 1

        for i in nums:
            if i < 0:
                dp[neg] = i
                neg += 2
            else:
                dp[pos] = i
                pos += 2

        return dp