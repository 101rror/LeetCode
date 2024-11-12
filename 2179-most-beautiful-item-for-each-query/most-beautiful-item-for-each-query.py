class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = itemgetter(0))

        maxbeauty, curbeauty = [0], 0

        for price, beauty in items:
            curbeauty = max(curbeauty, beauty)
            maxbeauty.append(curbeauty)

        ans = []

        for q in queries:
            i = bisect_right(items, q, key = itemgetter(0))
            ans.append(maxbeauty[i])

        return ans