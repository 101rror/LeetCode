class Solution:
    def isPalindrome(self, s: str) -> bool:
        strlist = []
        
        for char in s:
            if 'A' <= char <= 'Z':
                strlist.append(char.lower())
            elif 'a' <= char <= 'z' or '0' <= char <= '9':
                strlist.append(char)
            
        revlist = strlist[::-1]
                
        return strlist == revlist