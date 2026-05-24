class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        count = 0

        for num in nums:
            if count < k or num != nums[count - k]:
                nums[count] = num
                count += 1

        return nums[:count]
