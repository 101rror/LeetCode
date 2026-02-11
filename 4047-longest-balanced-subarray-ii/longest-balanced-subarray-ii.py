class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dct = {}
        ans = 0

        size = 4 * n
        segSum = [0] * size
        segMin = [0] * size
        segMax = [0] * size

        def pull(node):
            l, r = node * 2, node * 2 + 1
            segSum[node] = segSum[l] + segSum[r]
            segMin[node] = min(segMin[l], segSum[l] + segMin[r])
            segMax[node] = max(segMax[l], segSum[l] + segMax[r])

        def update(idx, val, node=1, l=0, r=n - 1):
            if l == r:
                segSum[node] = val
                segMin[node] = val
                segMax[node] = val
                return

            m = (l + r) // 2
            if idx <= m:
                update(idx, val, node * 2, l, m)
            else:
                update(idx, val, node * 2 + 1, m + 1, r)

            pull(node)

        def rightmost(target=0):
            def exist(node, sb):
                return segMin[node] <= target - sb <= segMax[node]

            def search(node=1, l=0, r=n - 1, sb=0):
                if not exist(node, sb):
                    return -1
                if l == r:
                    return l

                m = (l + r) // 2
                left = node * 2
                right = node * 2 + 1

                sbr = segSum[left] + sb
                if exist(right, sbr):
                    return search(right, m + 1, r, sbr)
                return search(left, l, m, sb)

            return search()

        for i in reversed(range(n)):
            x = nums[i]

            if x in dct:
                update(dct[x], 0)

            dct[x] = i

            dp[i] = 1 if x % 2 == 0 else -1
            update(i, dp[i])

            r = rightmost(0)
            if r >= i:
                ans = max(ans, r - i + 1)

        return ans
