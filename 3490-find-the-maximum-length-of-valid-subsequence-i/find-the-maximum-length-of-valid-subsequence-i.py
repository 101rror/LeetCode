class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        mx = max(even, odd)
        evendp = 0
        odddp = 0
        for num in nums:
            if num % 2 == 0:
                evendp = max(evendp, odddp + 1)
            else:
                odddp = max(odddp, evendp + 1)

        return max(mx, evendp, odddp)
