class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0

        for s in bank:
            count = s.count("1")
            if count:
                ans += prev * count
                prev = count

        return ans
