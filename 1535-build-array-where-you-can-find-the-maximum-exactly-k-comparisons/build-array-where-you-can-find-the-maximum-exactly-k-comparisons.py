class Solution(object):
    def numOfArrays(self, n, m, k):
        mod =  (10**9 + 7)

        @cache
        def bfs(index, cost, maximum):

            if (cost > k):
                return 0

            if (index >= n):
                if (cost != k):
                    return 0
                else:
                    return 1
                    
            res = 0

            for i in range(1, m + 1):
                res += bfs(index + 1, cost + 1 if i > maximum else cost, max(i, maximum))

            return res

        return bfs(0, 0, 0) % mod
        