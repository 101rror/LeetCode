class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new = list(map(str, nums))

        new.sort(key=lambda x: x*10, reverse=True)

        ans = ''

        for x in new:
            ans += x

        return ans if int(ans) > 0 else "0"