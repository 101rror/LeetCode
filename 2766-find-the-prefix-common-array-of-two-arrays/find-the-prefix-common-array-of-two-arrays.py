class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        common = 0
        ans = []

        for a, b in zip(A, B):
            freq[a] += 1
            if freq[a] == 2:
                common += 1
            
            freq[b] += 1
            if freq[b] == 2:
                common += 1

            ans.append(common)

        return ans
