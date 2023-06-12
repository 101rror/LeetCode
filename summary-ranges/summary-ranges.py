class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ans = []

        if (n == 0):
            return []

        j = 0
        l = 0
        
        for i in range(1, n):
            if (nums[i] - 1 != nums[i - 1]):

                if (nums[j] != nums[i - 1]):
                    ans.append("{}->{}".format(nums[j], nums[i - 1]))
                else:
                    ans.append(str(nums[j]))

                j = i
            l += 1 
        
        if (nums[j] != nums[l]):
            ans.append("{}->{}".format(nums[j], nums[l]))
        else:
            ans.append(str(nums[j]))

        return ans