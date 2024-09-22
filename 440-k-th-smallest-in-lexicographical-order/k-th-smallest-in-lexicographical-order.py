class Solution:
    def findKthNumber(self, num: int, k: int) -> int:
        def steps(n1, n2, num):
            count = 0

            while n1 <= num:
                count += min(n2, num + 1) - n1
                n1 *= 10
                n2 *= 10
            return count

        ans = 1
        k -= 1

        while k > 0:
            count = steps(ans, ans + 1, num)
            if count <= k:
                ans += 1
                k -= count
            else:
                ans *= 10
                k -= 1
        
        return ans
