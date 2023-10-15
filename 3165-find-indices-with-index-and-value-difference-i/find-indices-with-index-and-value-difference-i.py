class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        ans = []
        
        for i in range(n):
            for j in range(i + 1, n):
                if((abs(i - j) >= indexDifference) and (abs(nums[i] - nums[j]) >= valueDifference)):
                    ans.append(i)
                    ans.append(j)
                    
        if(len(ans) >= 2):
            return ans
        if(indexDifference == 0 and valueDifference == 0):
            return [0,0]
        else:
            return [-1,-1]