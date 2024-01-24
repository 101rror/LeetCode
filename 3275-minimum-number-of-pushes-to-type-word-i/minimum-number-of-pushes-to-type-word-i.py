class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        num = 2
        mp = defaultdict(str)

        for i in word:
            mp[num] += i
            num += 1
            if(num == 10):
                num = 2

        for i in word:
            for j in range(2, 10):
                if i in mp[j]:
                    ans += (mp[j].index(i) + 1)
                    break

        return ans
        