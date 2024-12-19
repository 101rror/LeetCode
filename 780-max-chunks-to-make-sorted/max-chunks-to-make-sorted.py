class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = dif = 0

        for idx, num in enumerate(arr):
            dif += num - idx
            if dif == 0:
                count += 1

        return count