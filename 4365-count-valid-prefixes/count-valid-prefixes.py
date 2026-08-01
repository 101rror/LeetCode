class Solution:
    def countValidPrefixes(self, s: str) -> int:
        count0 = count1 = ans = 0

        for ch in s:
            if ch == "0":
                count0 += 1
            else:
                count1 += 1

            if abs(count1 - count0) <= 1:
                ans += 1

        return ans
