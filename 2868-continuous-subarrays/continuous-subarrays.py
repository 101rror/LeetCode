class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        left = 0
        right = 0
        maxheap = []
        minheap = []

        while right < n:
            heappush(maxheap, (-nums[right], right))
            heappush(minheap, (nums[right], right))

            while maxheap and minheap and (-maxheap[0][0] - minheap[0][0]) > 2:
                left += 1
                while maxheap and maxheap[0][1] < left:
                    heappop(maxheap)
                while minheap and minheap[0][1] < left:
                    heappop(minheap)

            ans += (right - left + 1)
            right += 1

        return ans