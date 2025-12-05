class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(1, n):
            x = nums[0 : i]
            y = nums[i : n]
            xsum = sum(x)
            ysum = sum(y)

            if abs(ysum - xsum) % 2 == 0:
                count += 1

        return count
