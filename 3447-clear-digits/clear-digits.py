class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if "0" <= ch <= "9" and stack:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
