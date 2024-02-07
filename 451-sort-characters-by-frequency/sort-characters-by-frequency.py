class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        srt = sorted(cnt, key=cnt.get, reverse=True)
        ans = ""

        for i in srt:
            ans += i * cnt[i]

        return ans