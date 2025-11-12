class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if 1 in nums:
            return n - nums.count(1)

        gcdCount = 0
        for num in nums:
            gcdCount = gcd(gcdCount, num)

        if gcdCount > 1:
            return -1
        else:
            check = n
            for i in range(n):
                cur = 0
                for j in range(i, n):
                    cur = gcd(cur, nums[j])
                    if cur == 1:
                        check = min(check, j - i + 1)
                        break

            return check + n - 2
