class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(i):
                a = int(str(nums[i])[-1])
                b = int(str(nums[j])[0])

                if (math.gcd(a, b) == 1):
                    ans += 1
                    
        return ans