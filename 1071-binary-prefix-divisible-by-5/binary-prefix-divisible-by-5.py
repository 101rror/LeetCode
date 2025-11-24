class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        x = 0

        for num in nums:
            x = (x * 2 + num) % 5
            ans.append(x == 0)

        return ans
