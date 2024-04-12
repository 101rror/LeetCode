class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        for i in nums:
            if i > nums[ans]:
                ans += 1
                
        return ans
                
                    