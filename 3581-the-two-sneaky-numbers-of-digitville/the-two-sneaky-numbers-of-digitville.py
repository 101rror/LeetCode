class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []

        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                ans.append(num)

        return ans
