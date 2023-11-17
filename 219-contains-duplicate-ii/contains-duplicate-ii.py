class Solution:
    @staticmethod
    def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        mp = {}

        for i, num in enumerate(nums):
            if num in mp and i - mp[num] <= k:
                return True

            mp[num] = i

        return False