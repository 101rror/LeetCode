class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}

        for i in range(n - k + 1):
            for num in set(nums[i : i + k]):
                freq[num] = freq.get(num, 0) + 1

        ans = -1
        for num, count in freq.items():
            if count == 1 and num > ans:
                ans = num

        return ans
