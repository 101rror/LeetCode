class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        mp = {}
        max_num = max(groups)

        for i, e in enumerate(elements):
            num = e
            if e not in mp:
                while e <= max_num:
                    if e not in mp:
                        mp[e] = i
                    e += num

        res = []
        
        for e in groups:
            if e not in mp:
                res.append(-1)
            else:
                res.append(mp[e])

        return res
