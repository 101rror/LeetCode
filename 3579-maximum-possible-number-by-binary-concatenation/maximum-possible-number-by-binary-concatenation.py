class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a, b, c = [bin(num)[2:] for num in nums]

        binary = [a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a]

        return max(int(num, 2) for num in binary)
