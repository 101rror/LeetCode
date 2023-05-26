class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealth = max([reduce((lambda x, y : x + y), a) for a in accounts])

        return wealth