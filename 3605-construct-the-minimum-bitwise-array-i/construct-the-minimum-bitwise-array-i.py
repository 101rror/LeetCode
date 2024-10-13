class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                for k in range(num):
                    if (k | (k + 1)) == num:
                        ans.append(k)
                        break
        
        return ans