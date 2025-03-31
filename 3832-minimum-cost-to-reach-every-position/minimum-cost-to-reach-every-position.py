class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        return list(accumulate(cost, min))
