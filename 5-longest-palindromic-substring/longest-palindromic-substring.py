class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s):
            return s == s[::-1]

        ans = []
        n = len(s)

        for i in range (0, n):
            for j in range (i, n):
                sstr = s[i : j + 1]

                if palindrome(sstr):
                    if len(ans) > len(sstr):
                        continue
                    else:
                        ans = sstr

        return ans