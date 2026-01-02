class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        n //= 2

        counter = Counter(nums)

        for key, val in counter.items():
            if val == n:
                return key
