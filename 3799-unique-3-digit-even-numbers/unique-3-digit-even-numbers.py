class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        nums = set()

        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                nums.add((a, b, c))

        return len(nums)
