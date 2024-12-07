class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        
        while low < high:
            mid = (low + high) // 2
            if sum((num - 1) // mid for num in nums) <= maxOperations:
                high = mid
            else:
                low = mid + 1
        
        return high