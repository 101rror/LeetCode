class Solution:
    def findMin(self, nums: List[int]) -> int:
        first, last = 0, len(nums) - 1

        while first < last:
            mid = first + (last - first) // 2

            if nums[mid] < nums[last]:
                last = mid
            elif nums[mid] > nums[last]:
                first = mid + 1
            else:
                last -= 1

        return nums[first]
