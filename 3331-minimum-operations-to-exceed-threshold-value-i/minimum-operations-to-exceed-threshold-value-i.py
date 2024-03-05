class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        
        for i in nums:
            if i < k:
                count += 1
                
        return count