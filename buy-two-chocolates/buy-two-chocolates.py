class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        ln = len(prices)
        prices = sorted(prices)
        
        check = (prices[0] + prices[1])
        
        if(check == money):
            return 0
        elif(check > money):
            return money
        else:
            return (money - check)