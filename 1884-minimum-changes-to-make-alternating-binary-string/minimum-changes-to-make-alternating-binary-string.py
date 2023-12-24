class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        count = 0
        count1 = 0
        if(s.count('1') == n or s.count('0') == n):
            return n // 2

        f = s[0]

        for i in range(n):
            if(i % 2 == 0):
                if(f != s[i]):
                    count += 1
            else:
                if(f == s[i]):
                    count += 1

        for i in range(n):
            if(i % 2 == 0):
                if(f == s[i]):
                    count1 += 1
            else:
                if(f != s[i]):
                    count1 += 1

        return min(count, count1)