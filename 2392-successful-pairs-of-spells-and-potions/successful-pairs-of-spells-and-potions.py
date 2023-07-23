class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        ans = []
        n = len(potions)

        for i in spells:
            val = (success // i)

            if (success % i == 0):
                idx = bisect.bisect_left(potions, val)

            else:    
                idx = bisect.bisect_right(potions, val)

            ans.append(n - idx)

        return ans