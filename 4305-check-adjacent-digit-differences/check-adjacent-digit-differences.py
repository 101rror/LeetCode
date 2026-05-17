class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        lst = []

        for x in s:
            lst.append(int(x))

        for i in range(1, len(lst)):
            if abs(lst[i - 1] - lst[i]) > 2:
                return False

        return True
