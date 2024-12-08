class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set(nums)
        count = 0

        for num in st:
            if num < k:
                return -1
            if num > k:
                count += 1

        return count