class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        n = len(arr)

        for i in arr:
            freq[i] += 1

        per = n // 4

        for i in freq:
            if(freq[i] > per):
                return i
