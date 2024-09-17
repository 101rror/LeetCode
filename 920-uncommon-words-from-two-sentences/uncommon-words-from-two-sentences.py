class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        news1 = s1.split()
        news2 = s2.split()
        newstr = news1 + news2
        ans = []

        Count = Counter(newstr)

        for word in Count:
            if Count[word] == 1:
                ans.append(word)

        return ans