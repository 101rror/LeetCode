class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        xor1, xor2, ans = 0, 0, 0

        for num1 in nums1:
            xor1 ^= num1

        for num2 in nums2:
            xor2 ^= num2

        if n1 % 2 == 1:
            ans ^= xor2
        if n2 % 2 == 1:
            ans ^= xor1

        return ans
