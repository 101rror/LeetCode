class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n):
            for j in range(i + 1, n):
                x = i * i + j * j
                c = int(x**0.5)

                if c * c == x and c <= n:
                    count += 2

        return count
