class Solution:
    def find132pattern(self, nums):
        lst = list(accumulate(nums, min))
        stack, n = [], len(nums)
        
        for j in range(n - 1, -1, -1):
            if (nums[j] > lst[j]):
                while (stack and stack[-1] <= lst[j]):
                    stack.pop()
                if (stack and stack[-1] < nums[j]):
                    return True

                stack.append(nums[j]) 

        return False
        