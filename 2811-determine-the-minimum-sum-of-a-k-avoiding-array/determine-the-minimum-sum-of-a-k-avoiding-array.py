class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        st = set()
        curr, ans = 1, 0

        while(n > 0):
            if(k - curr not in st):
                ans += curr
                n -= 1
                st.add(curr)
            curr += 1
        return ans