class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        lst = []
        ns = ''
        i = 0

        for letter in s:
            if letter in vowel:
                lst.append(letter)

        for letter in s:
            if letter in vowel:
                ns += lst[-1]
                lst.pop(-1)
            else:
                ns += letter

        return ns