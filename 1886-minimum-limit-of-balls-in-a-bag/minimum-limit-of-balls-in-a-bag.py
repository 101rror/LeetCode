class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isPenalty(mid):
            op = 0
            for num in nums:
                if num > mid:
                    op += (num - 1) // mid
                if op > maxOperations:
                    return False

            return True
            
        low, high = 1, max(nums)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            if isPenalty(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result