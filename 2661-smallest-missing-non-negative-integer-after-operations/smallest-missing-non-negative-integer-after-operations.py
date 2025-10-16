class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        freq = Counter()

        for num in nums:
            rem = num % value
            freq[rem] += 1

        for i in range(n + 1):
            rem = i % value
            if freq[rem] == 0:
                return i

            freq[rem] -= 1
