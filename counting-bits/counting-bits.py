class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(0, n + 1):
            x = bin(i)
            x = (i.bit_count())
            ans.append(x)

        return ans