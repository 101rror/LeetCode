class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)
        x = n // 3
        ans = []

        for num in nums:
            c = nums.count(num) 
            if(c > x):
                ans.append(num)

        s = list(set(ans))

        return s
