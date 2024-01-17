class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        def isunique(lst):
            for i in range(1, len(lst)):
                if(lst[i - 1] == lst[i]):
                    return False
            return True

        mp = defaultdict(int)
        ans = []

        for i in arr:
            mp[i] += 1

        for i in mp.values():
            ans.append(i)

        ans.sort()

        if(isunique(ans)):
            return True
        else:
            return False