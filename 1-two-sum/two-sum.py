class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, num in enumerate(nums):
            check = target - num

            if check in hashmap:
                return [hashmap[check], idx]

            hashmap[num] = idx