class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if 5 <= purchaseAmount%10:
            return 100 - math.ceil(purchaseAmount/10)*10
            
        return 100 - math.floor(purchaseAmount/10)*10