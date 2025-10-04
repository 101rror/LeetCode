class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n - 1
        ans = 0

        while left < right:
            mn = min(height[left], height[right])
            dif = right - left
            ans = max(ans, (mn * dif))

            if(height[left] > height[right]):
                right -= 1
            else:
                left += 1

        return ans