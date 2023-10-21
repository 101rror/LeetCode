class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque([])

        for i, n in enumerate(nums):
            while q and q[0] < i - k:
                q.popleft()
            if q:
                nums[i] = max(nums[i], nums[i] + nums[q[0]])

            while q and nums[q[-1]] < nums[i]:
                q.pop()
            if nums[i] > 0:
                q.append(i)
                
        return max(nums)