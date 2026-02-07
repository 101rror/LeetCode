class Solution:
    def checkString(self, s: str) -> bool:
        stack = []

        for ch in s:
            if stack and ch == "a" and stack[-1] == "b":
                return False
            else:
                stack.append(ch)

        return True
