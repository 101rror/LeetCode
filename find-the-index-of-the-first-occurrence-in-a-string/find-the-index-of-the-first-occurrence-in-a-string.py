class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)

        if (len1 == 0 or len2 == 0):
            return 0

        if needle not in haystack:
            return -1
            
        else:
            return haystack.index(needle)