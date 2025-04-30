class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for num in nums:
            x = str(num)

            if len(x) % 2 == 0:
                count += 1

        return count
