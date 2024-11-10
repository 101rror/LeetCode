class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        def increase(i: int) -> bool:
            for i in range(i, i + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        for i in range(n - 2 * k + 1):
            if increase(i) and increase(i + k):
                return True
        
        return False