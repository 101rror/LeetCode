class Solution:
    def bestClosingTime(self, customers: str) -> int:
        mx = score = 0
        ans = -1

        for i, c in enumerate(customers):
            if c == "Y":
                score += 1
            else:
                score -= 1

            if score > mx:
                mx, ans = score, i

        return ans + 1
