class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        first = 0
        last = n

        while(first <= last):
            mid = (first + last) // 2
            count = 0 
            for i in nums:
                if(i >= mid):
                    count +=1

            if (count == mid):
                return mid
            elif (count > mid):
                first = mid + 1
            else : 
                last = mid - 1

        return -1            