class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()

        def countpair(target):
            count = 0
            first = 0
            last = n - 1

            while first < last:
                if nums[first] + nums[last] <= target:
                    count += (last - first)
                    first += 1
                else:
                    last -= 1
            return count

        totalupper = countpair(upper)
        totallower = countpair(lower - 1)
        ans = totalupper - totallower

        return ans