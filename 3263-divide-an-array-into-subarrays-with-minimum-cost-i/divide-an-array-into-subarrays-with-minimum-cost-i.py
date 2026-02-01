class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[0]
        fi, se = 51, 51

        for i in range(1, n):
            if nums[i] < fi:
                se = fi
                fi = nums[i]
            elif nums[i] < se:
                se = nums[i]

        return first + se + fi
