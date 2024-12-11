class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)

        rng = [0] * (mx + 10)

        for num in nums:
            left = max(0, num - k)
            right = min(mx, num + k) + 1
            rng[left] += 1
            rng[right] -= 1


        for i in range(1, len(rng)):
            rng[i] += rng[i - 1]
     
        return max(rng)