class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low, high = 1, max(quantities)
        count = 0

        while low <= high:
            mid = low + (high - low) // 2
            need = sum(math.ceil(x / mid) for x in quantities)

            if need <= n:
                count = mid
                high = mid - 1
            else:
                low = mid + 1

        return count