class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int: 
        n = len(nums)
        ans =- 1
        
        for i in range(n):
            p =- 1
            for j in range(i + 1, n):
                if(nums[j] - nums[j - 1] != p * (-1)):
                    break
                else:
                    ans = max(ans, j - i + 1)
                    p *= -1
        return ans