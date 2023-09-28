class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        count = 0

        for i in range(n):
            x = nums[i]
            if(x <= 0):
                continue
            else:
                for j in range(n):
                    nums[j] -= x
                count += 1

        return count        