class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst = list(sentence.split())

        for i, word in enumerate(lst):
            if word.startswith(searchWord):
                return i + 1

        return -1