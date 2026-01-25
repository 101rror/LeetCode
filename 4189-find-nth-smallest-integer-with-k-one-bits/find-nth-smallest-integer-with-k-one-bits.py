class Solution:
    def nthSmallest(self, n: int, k: int) -> int:
        rem, ans, pos = n, 0, k - 1

        while True:
            x = math.comb(pos, k - 1)
            if rem > x:
                rem -= x
                pos += 1
            else:
                break

        ans |= 1 << pos
        left = k - 1

        while left > 0:
            c = left - 1
            while True:
                x = math.comb(c, left - 1)
                if rem > x:
                    rem -= x
                    c += 1
                else:
                    break

            ans |= 1 << c
            left -= 1

        return ans
