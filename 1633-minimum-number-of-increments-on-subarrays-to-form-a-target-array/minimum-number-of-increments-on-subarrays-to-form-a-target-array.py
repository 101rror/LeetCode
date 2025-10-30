class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        res = 0

        for num in target:
            if num > prev:
                diff = num - prev
                res += diff
            prev = num

        return res
