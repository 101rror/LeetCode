class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        sum = s.count('1', 1)

        if s[0] == '0':
            sum += 1

        ans = sum

        for c in s[1 : n - 1]:
            if c == '0':
                sum += 1
            else:
                sum -= 1

            ans = max(ans, sum)
            
        return ans
        