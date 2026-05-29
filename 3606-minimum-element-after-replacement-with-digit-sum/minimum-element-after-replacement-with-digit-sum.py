class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        ans = []

        for num in nums:
            x = str(num)
            tsum = 0
            for i in x:
                tsum += int(i)

            ans.append(tsum)

        return min(ans)
