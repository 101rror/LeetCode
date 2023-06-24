from collections import defaultdict

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0

        for rod in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                new_dp[diff + rod] =  max(taller+rod, new_dp[diff+rod])
                new_dp[abs(diff-rod)] = max(new_dp[abs(diff-rod)], taller-diff+rod, taller)

            dp = new_dp
    
        
        return dp[0]
