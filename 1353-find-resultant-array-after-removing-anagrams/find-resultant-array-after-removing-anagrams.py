class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        mp = defaultdict(int)
        ans = []
        prev = words[0]

        for word in words:
            srt = "".join(sorted(word))
            if srt not in mp:
                mp[srt] == 1
                ans.append(word)
            elif prev != srt:
                ans.append(word)

            prev = srt

        return ans
