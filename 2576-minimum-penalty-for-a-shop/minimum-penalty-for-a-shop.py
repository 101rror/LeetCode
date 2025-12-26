class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        mx = score = 0
        ans = -1

        for i in range(n):
            if customers[i] == "Y":
                score += 1
            else:
                score -= 1

            if score > mx:
                mx, ans = score, i

        return ans + 1
