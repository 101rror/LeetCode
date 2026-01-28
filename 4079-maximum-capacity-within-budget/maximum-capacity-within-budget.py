class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)
        v = [(costs[i], capacity[i]) for i in range(n)]
        v.sort()

        ans, cnt = 0, 1

        while cnt < n:
            cnt <<= 1

        dp = [0] * (2 * cnt)
        for i in range(n):
            dp[cnt + i] = v[i][1]
        for i in range(cnt - 1, 0, -1):
            dp[i] = max(dp[2 * i], dp[2 * i + 1])

        def query(left, right):
            res = 0
            left += cnt
            right += cnt
            while left <= right:
                if left & 1:
                    res = max(res, dp[left])
                    left += 1
                if not (right & 1):
                    res = max(res, dp[right])
                    right -= 1
                left >>= 1
                right >>= 1

            return res

        for i in range(n):
            cost, cap = v[i]
            if cost < budget:
                ans = max(ans, cap)

            rem = budget - cost
            idx = bisect.bisect_left(v, (rem, -1)) - 1
            if idx > i:
                ans = max(ans, cap + query(i + 1, idx))

        return ans
