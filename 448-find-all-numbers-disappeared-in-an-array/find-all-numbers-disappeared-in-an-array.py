class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash = {}
        ans = []
        
        for num in nums:
            hash[num] = 1
        
        for num in range(1, len(nums) + 1):
            if num not in hash:
                ans.append(num)
        
        return ans