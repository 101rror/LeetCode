class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxcount = 0
        count = 0
        mp = {0:-1}  

        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in mp:
                maxcount = max(maxcount, i - mp[count])
            else:
                mp[count] = i

        return maxcount     