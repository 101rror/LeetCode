class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        fi = s[:n // 2]
        se = s[n // 2:]
        vowel = "aeiouAEIOU"
        cntfi, cntse = 0, 0

        for i in fi:
            if i in vowel:
                cntfi += 1
        for i in se:
            if i in vowel:
                cntse += 1
        
        if(cntfi == cntse):
            return True