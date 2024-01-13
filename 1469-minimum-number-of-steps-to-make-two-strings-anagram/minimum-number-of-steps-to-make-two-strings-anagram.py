class Solution:
    def minSteps(self, s: str, t: str) -> int:
        n = len(s)
        mp = defaultdict(int)
        count = 0
        
        for i in s:
            mp[i] += 1

        for i in t:
            if mp[i]:
                mp[i] -= 1
            else:
                count += 1

        return count