class Solution:
    def maxRunTime(self, n: int, arr: List[int]) -> int:
        arr.sort()
        tsum = sum(arr)

        while arr[-1] > tsum // n:
            tsum -= arr.pop()
            n -= 1

        return tsum // n
