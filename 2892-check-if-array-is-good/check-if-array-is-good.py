class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maximum = max(nums)

        if(len(nums) != maximum + 1):
            return False

        else:
            nums1 = set(nums)

            for i in nums1:
                if(i == maximum):
                    continue
                if(nums.count(i) > 1):
                    return False
                
            if(nums.count(maximum) == 2):
                return True
                
        return False