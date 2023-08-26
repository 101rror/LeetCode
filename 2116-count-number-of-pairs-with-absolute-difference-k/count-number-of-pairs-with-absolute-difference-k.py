class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        count = 0

        for i in range(0, n - 1):
            for j in range(i + 1, n):
                x = abs(nums[i] - nums[j])
                if(x == k):
                    count += 1

        return count
