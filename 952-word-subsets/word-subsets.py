class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = set(words1)
        freq = {}

        for word in words2:
            for ch in word:
                count = word.count(ch)
                if ch not in freq or count > freq[ch]:
                    freq[ch] = count

        for word in words1:
            for ch in freq:
                if word.count(ch) < freq[ch]:
                    ans.remove(word)
                    break

        return list(ans)
