class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        k = len(pizzas) // 4
        gap = k // 2
        ans = 0

        for i, x in enumerate(reversed(nlargest(k + gap, pizzas))):
            if i & 1 and gap:
                gap -= 1
            else:
                ans += x

        return ans
