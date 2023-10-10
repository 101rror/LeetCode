class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(set(nums))
        nums = sorted(nums)
        first = 0
        count = n

        while(first < len(nums)):
            last = nums[first] + n - 1
            x = bisect_right(nums, last)

            count = min(count, (n - (x - first)))

            first +=1

        return count
