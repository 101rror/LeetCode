class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        ans = []

        for kk, v in counter.items():
            nk = k
            if v <= nk:
                while v:
                    ans.append(kk)
                    v -= 1
            else:
                while nk:
                    ans.append(kk)
                    nk -= 1

        return ans
