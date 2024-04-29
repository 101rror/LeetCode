class Solution:
    def minEnd(self, n: int, x: int) -> int:
        nums = []

        for i in range(64):
            if x >> i & 1 ^ 1:
                nums.append(i)

        last = n - 1

        for i in range(len(nums)):
            if last >> i & 1:
                x |= 1 << nums[i]

        return x
