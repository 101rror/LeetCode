class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def checkdistinct(arr):
            counter = Counter(arr)

            for val in counter.values():
                if val > 1:
                    return False

            return True

        count = 0
        n = len(nums)

        if checkdistinct(nums):
            return count
        if n < 3:
            return 1

        count += 1

        for i in range(3, n, 3):
            if checkdistinct(nums[i:n]):
                return count
            else:
                count += 1

        return count
