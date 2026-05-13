class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            diff[a + 1] -= 1
            diff[b + limit + 1] += 1

            diff[a + b] -= 1
            diff[a + b + 1] += 1

        pair = n // 2
        curr = pair * 2
        ans = float("inf")

        for tSum in range(2, 2 * limit + 1):
            curr += diff[tSum]
            ans = min(ans, curr)

        return ans
