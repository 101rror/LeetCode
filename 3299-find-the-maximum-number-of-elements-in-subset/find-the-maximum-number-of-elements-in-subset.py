class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counter = Counter(nums)

        one = counter.get(1, 0)
        ans = one if one % 2 else one - 1

        counter.pop(1, None)

        for num in counter:
            res = 0
            x = num
            while x in counter and counter[x] > 1:
                res += 2
                x *= x
            ans = max(ans, res + (1 if x in counter else -1))

        return ans
