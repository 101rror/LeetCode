class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def BinarySearch(arr):
            n = len(arr)
            count = 0

            first = 0
            last = n - 1

            while first <= last:
                mid = (first + last) // 2

                if arr[mid] < 0:
                    last = mid - 1
                else:
                    first = mid + 1

            return first

        count = 0

        for lst in grid:
            count += len(lst) - BinarySearch(lst)

        return count
