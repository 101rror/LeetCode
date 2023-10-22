class Solution:
    def maximumScore(self, nums, k):
        ans = 0
        q = deque()
   
        for j in range(len(nums)):
            n = nums[j]
            i = j
            while q and q[-1][1] >= n:
                i, val = q.pop()
                if i<=k and j-1 >= k:
                    ans = max(ans, val*(j-i))
            q.append((i, n))

        j = len(nums)

        for i,val in q:
            if i<=k and j-1 >=k:
                ans = max(ans, val * (j-i))

        return ans