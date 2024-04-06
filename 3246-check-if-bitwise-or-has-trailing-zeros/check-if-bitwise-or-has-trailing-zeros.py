class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
		
        for n in nums:
            if n % 2 == 0: 
                count += 1
            if count > 1:
                return True