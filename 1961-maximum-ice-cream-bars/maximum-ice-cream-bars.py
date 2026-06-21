class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()

        for cost in costs:
            if cost <= coins:
                count += 1
                coins -= cost
            else:
                break

        return count
