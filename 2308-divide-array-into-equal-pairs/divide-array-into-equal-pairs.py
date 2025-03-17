class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        if len(nums) % 2 != 0:
            return False

        for val in counter.values():
            if val % 2 != 0:
                return False

        return True
