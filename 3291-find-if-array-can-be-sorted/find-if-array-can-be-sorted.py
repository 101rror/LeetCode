class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        i = last = 0

        while i < len(nums):
            x = nums[i].bit_count()
            Min = Max = nums[i]
            j = i + 1

            while j < len(nums) and nums[j].bit_count() == x:
                Min = min(Min, nums[j])
                Max = max(Max, nums[j])
                j += 1

            if last > Min:
                return False

            i, last = j, Max
            
        return True