class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def expand_around_center(s: str, left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  

        max_length = 0
        n, m = len(s), len(t)

       
        for i in range(n + 1):  
            for j in range(m + 1): 
                combined = s[:i] + t[j:] 

                for center in range(len(combined)):
                    len1 = expand_around_center(combined, center, center)  
                    len2 = expand_around_center(combined, center, center + 1)
                    max_length = max(max_length, len1, len2)

        return max_length