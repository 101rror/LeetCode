class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weights = {}
        for item in (items1 + items2):
            value, weight = item[0], item[1]
            weights[value] = weights.get(value, 0) + weight

        return sorted(list(weights.items()))