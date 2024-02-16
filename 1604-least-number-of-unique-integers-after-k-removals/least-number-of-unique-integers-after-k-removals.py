class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mp = Counter(arr)

        sortmp = sorted(mp.items(), key=lambda x: x[1])

        for key, value in sortmp:
            if k >= value:
                k -= value
                del mp[key]
            else:
                break

        return len(mp)