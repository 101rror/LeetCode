class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans, mx = 0, neededTime[0]

        for i in range(1, n):
            if colors[i - 1] == colors[i]:
                mn = min(mx, neededTime[i])
                ans += mn
                mx = max(mx, neededTime[i])
            else:
                mx = neededTime[i]

        return ans
