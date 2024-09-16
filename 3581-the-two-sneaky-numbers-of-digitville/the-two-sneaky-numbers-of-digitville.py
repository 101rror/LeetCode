class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic = {}
        ans = []
        
        for num in nums:
            if num in dic:
                ans.append(num)
            else:
                dic[num] = 1
                
        return ans