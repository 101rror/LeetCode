class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedarr = sorted(set(arr))
        index = []
        rank = {}

        for idx, value in enumerate(sortedarr):
            rank[value] = idx + 1

        for num in arr:
            index.append(rank[num])

        return index
