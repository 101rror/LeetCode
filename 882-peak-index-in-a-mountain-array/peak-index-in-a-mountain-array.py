class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        first = 1
        last = (n - 1)

        while(first < last):
            mid = (first + last) // 2

            if(arr[mid] < arr[first] and arr[mid] < arr[last]):
                return mid

            if(arr[mid] < arr[mid + 1]):
                first = mid + 1

            else:
                last = mid

        return first