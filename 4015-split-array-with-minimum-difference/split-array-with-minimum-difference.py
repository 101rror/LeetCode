class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        tSum = sum(nums)
        suffix = [0] * n
        suffix[-1] = 1

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] and (nums[i] > nums[i + 1])

        ans = float("inf")

        lSum = 0
        left = 1
        for i in range(n - 1):
            lSum += nums[i]
            if i == 0:
                left = 1
            else:
                if not (nums[i] > nums[i - 1]):
                    left = 0

            if left and suffix[i + 1]:
                rSum = tSum - lSum
                diff = abs(lSum - rSum)
                if diff < ans:
                    ans = diff

        return -1 if ans == float("inf") else ans
