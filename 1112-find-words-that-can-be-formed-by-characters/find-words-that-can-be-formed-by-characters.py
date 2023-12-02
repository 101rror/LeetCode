class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = collections.Counter(chars)
        ans = (len(word) for word in words if all(freq[char] >= word.count(char) for char in word))

        tsum = sum(ans)

        return tsum