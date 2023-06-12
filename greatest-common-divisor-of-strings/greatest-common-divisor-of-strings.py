class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        str3 = ""

        if (len1 == len2):
            if (str1 == str2):
                return str1
            else:
                return str3
        else:
            if (len1 < len2):
                str1,str2 = str2,str1

            if (str1[:len(str2)] == str2):
                return self.gcdOfStrings(str1[len(str2):], str2)
                
            else:
                return str3