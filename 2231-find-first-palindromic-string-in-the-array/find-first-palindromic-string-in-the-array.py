class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def ispalindrom(s):
            return s == s[::-1]

        for i in words:
            if(ispalindrom(i)):
                return i

        return ""