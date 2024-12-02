class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        lst = list(sentence.split())
        ans = -1

        for i in range(len(lst)):
            check = lst[i]
            if check.find(searchWord) != -1 and check[0] == searchWord[0] and check[n - 1] == searchWord[n - 1]:
                ans = i + 1
                break

        return ans