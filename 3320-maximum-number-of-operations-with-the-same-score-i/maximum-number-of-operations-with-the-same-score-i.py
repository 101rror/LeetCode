from collections import deque

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        if(n < 2):
            return 0
        count, s = 1, (nums[0] + nums[1])
        
        q = deque()
        
        for i in range(2, n):
            q.append(nums[i])
            
        while(len(q) > 1):
            a = q.popleft()
            b = q.popleft()
            
            if(a + b == s):
                count += 1
            else:
                return count
            
        return count
        