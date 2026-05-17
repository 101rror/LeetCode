class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)

        def dfs(i: int) -> bool:
            if i < 0 or i >= n or arr[i] < 0:
                return False

            if arr[i] == 0:
                return True

            arr[i] *= -1

            left = dfs(i + arr[i])
            right = dfs(i - arr[i])

            return left or right

        return dfs(start)
