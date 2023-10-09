class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        no = [-1, -1]

        def search(check):
            first = 0
            last = n

            while (first < last):
                mid = (first + last) // 2
                
                if (nums[mid] < check):
                    first = (mid +1)
                else:
                    last = mid                    
            return first
        
        first = search(target)
        last = search(target + 1) - 1
        
        if (first <= last):
            ans.append(first)
            ans.append(last)
            return ans
            
        else:        
            return no