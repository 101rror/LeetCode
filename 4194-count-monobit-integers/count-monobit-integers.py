class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0

        for i in range(n + 1):
            bit = bin(i)[2:]
            ln = len(bit)
            z, o = bit.count("0"), bit.count("1")

            if z == ln or o == ln:
                count += 1

        return count
