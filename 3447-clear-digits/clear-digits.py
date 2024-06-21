class Solution:
    def clearDigits(self, s: str) -> str:
        st = []

        for ch in s:
            if '0' <= ch <= '9' and st:
                st.pop()
            else:
                st.append(ch)
        
        s = "".join(st)
        
        return s