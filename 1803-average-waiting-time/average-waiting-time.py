class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        at = 0
        tw = 0

        for arr, t in customers:
            at = max(at, arr) + t
            tw += (at - arr)

        ans = tw / n

        return ans

            