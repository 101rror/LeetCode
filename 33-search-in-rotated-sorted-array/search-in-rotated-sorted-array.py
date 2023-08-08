class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        first = 0
        last = (n - 1)

        while(first <= last):
            mid = (first + last) // 2

            if (nums[mid] == target):
                return mid
            
            elif ((nums[first] < nums[mid] and nums[first] <= target < nums[mid]) or (nums[first] > nums[mid] and (target < nums[mid] or target >= nums[first]))):
                last = (mid - 1)
                  
            else:
                first = (mid + 1)
        return -1