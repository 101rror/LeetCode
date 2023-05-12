class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(0, n - 1):
            j = (i + 1)
            while(j < n):
                check = nums[i] + nums[j]
                if(check == target):
                    ans = i, j
                j += 1

        return ans