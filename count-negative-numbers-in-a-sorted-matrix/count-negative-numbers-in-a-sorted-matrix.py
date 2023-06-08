class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def BinarySearch(array):
            n = len(array)
            count = 0

            first = 0
            last = (n - 1)

            while(first <= last):
                mid = (first + last) // 2

                if(array[mid] < 0):
                    last = (mid - 1)

                elif(array[mid] >= 0):
                    first = (mid + 1)

            return first
            
        count = 0

        for i in grid:
            count = count + len(i) - BinarySearch(i)

        return count