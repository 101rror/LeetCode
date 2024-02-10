class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            return s == s[::-1]
        def substr(s):
            if len(s) == 0:
                return []
            elif len(s) == 1:
                return [s]
            else:
                ans = []
         
            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if isPalindrome(s[i : j]):
                        ans.append(s[i : j])

            return ans

        

        new = substr(s)

        return len(new)