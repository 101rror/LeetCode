class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0

        for b in s:
            if b == "(":
                stack.append(b)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return len(stack) + count