class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for key, value in counter.items():
            if value >= 2:
                return True

        return False