class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        st = set()
        ans = 0

        for w in words:
            if w in st:
                ans += 1
            else:
                st.add(w[::-1])

        return ans