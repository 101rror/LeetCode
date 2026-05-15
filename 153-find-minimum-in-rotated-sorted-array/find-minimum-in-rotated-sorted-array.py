class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        first = 0
        last = n - 1

        while first < last:
            mid = (first + last) // 2

            if nums[mid] > nums[last]:
                first = mid + 1

            else:
                last = mid

        return nums[first]
