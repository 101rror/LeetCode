class Solution:
    def maxRunTime(self, n: int, arr: List[int]) -> int:
        arr.sort()
        tsum = sum(arr)

        while arr[-1] > tsum // n:
            n -= 1
            tsum -= arr.pop()

        return tsum // n
