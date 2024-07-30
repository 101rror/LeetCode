class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        stack = []

        for x in s:
            if stack and x == 'a' and stack[-1] == 'b':
                stack.pop()
                count += 1

            else:
                stack.append(x)

        return count
