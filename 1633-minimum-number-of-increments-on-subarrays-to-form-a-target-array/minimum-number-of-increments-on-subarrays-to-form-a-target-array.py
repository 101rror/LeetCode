class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev, ans = 0, 0

        for num in target:
            if num > prev:
                diff = num - prev
                ans += diff
            prev = num

        return ans
