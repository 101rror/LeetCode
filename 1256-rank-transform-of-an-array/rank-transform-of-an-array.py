class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sarr = sorted(arr)

        freq = {}
        curr = 1

        for num in sarr:
            if num not in freq:
                freq[num] = curr
                curr += 1

        return [freq[num] for num in arr]
