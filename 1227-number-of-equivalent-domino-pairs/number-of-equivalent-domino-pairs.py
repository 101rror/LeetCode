class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        count = 0

        for x, y in dominoes:
            val = 0
            if x <= y:
                val = x * 10 + y
            else:
                val = y * 10 + x

            count += num[val]
            num[val] += 1

        return count
