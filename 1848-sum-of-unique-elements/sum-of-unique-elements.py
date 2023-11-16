class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums.sort()
        a = []
        ans = 0

        for i in range(len(nums) - 1):
            if(nums[i] == nums[i + 1]):
                a.append(nums[i])

        for i in nums:
            if i not in a:
                ans += i
            else:
                continue

        return ans