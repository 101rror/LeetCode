class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        st = set(banned)
        cursum = 0
        count = 0

        for i in range(1, n + 1):
            if i not in st:
                cursum += i
                if cursum <= maxSum:
                    count += 1
                else:
                    break


        return count