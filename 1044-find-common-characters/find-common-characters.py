class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = Counter(words[0])

        for word in words:
            freq &= Counter(word)

        return list(freq.elements())