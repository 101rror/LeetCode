class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        counter = Counter(banned)
        cursum = 0
        count = 0

        for i in range(1, n + 1):
            if i not in counter:
                cursum += i
                if cursum <= maxSum:
                    count += 1
                else:
                    break


        return count