class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        str1 = sentence1.split()
        str2 = sentence2.split()
        len1 = len(str1)
        len2 = len(str2)

        if len1 > len2:
            len1, len2 = len2, len1
            str1, str2 = str2[:], str1[:]

        count = 0
        while count < len1 and str1[count] == str2[count]:
            count += 1
        while count < len1 and str1[count] == str2[len2 - len1 + count]:
            count += 1

        return count == len1