class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        idx = []

        def isPrime(n):
            if n == 2 or n == 3:
                return True
            if n % 2 == 0 or n < 2:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False    

            return True

        for i in range(len(nums)):
            if isPrime(nums[i]):
                idx.append(i)

        mn = min(idx)
        mx = max(idx)

        return abs(mn - mx)