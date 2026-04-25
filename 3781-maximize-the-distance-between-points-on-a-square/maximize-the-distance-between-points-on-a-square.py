class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        arr = []

        for x, y in points:
            if y == 0:
                arr.append(x)
            elif x == side:
                arr.append(side + y)
            elif y == side:
                arr.append(3 * side - x)
            else:
                arr.append(4 * side - y)

        arr.sort()
        n = len(arr)

        brr = arr + [p + 4 * side for p in arr]

        def isValid(d: int) -> bool:
            nxt = [2 * n] * (2 * n + 1)
            j = 0

            for i in range(2 * n):
                while j < 2 * n and brr[j] - brr[i] < d:
                    j += 1
                nxt[i] = j

            limit = 4 * side - d
            for i in range(n):
                if i < n - 1 and nxt[i] == nxt[i + 1]:
                    continue

                curr = i
                for _ in range(k - 1):
                    curr = nxt[curr]

                if curr < 2 * n and brr[curr] - brr[i] <= limit:
                    return True

            return False

        low, high = 1, side
        ans = 1

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
