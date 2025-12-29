class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)

        for rule in allowed:
            mp[rule[:2]].append(rule[2])

        def dfs(row: str) -> bool:
            if len(row) == 1:
                return True
            nxt = [""]

            for i in range(len(row) - 1):
                pair = row[i : i + 2]
                if pair not in mp:
                    return False

                new = []
                for pref in nxt:
                    for ch in mp[pair]:
                        new.append(pref + ch)
                nxt = new

            for nr in nxt:
                if dfs(nr):
                    return True

            return False

        return dfs(bottom)
