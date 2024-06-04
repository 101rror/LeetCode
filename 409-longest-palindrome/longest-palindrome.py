class Solution:
    def longestPalindrome(self, s: str) -> int:
        def Palindrome(s):
            ss = set()
            for letter in s:
                if letter not in ss:
                    ss.add(letter)
                else:
                    ss.remove(letter)
            if len(ss) != 0:
                return len(s) - len(ss) + 1
            else:
                return len(s)

        return Palindrome(s)