import math

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        mp = {}
        mx = -1

        for num in nums:
            sqrt = isqrt(num)

            if sqrt * sqrt == num and sqrt in mp:
                mp[num] = mp[sqrt] + 1
            else:
                mp[num] = 1


        return max(mp.values()) if max(mp.values()) > 1 else -1