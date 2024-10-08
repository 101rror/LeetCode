class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))', '}')
        stack = []
        countRight = 0
        countLeft = 0

        for b in s:
            if b == ")" or b == "}":
                if b == ")":
                    countRight += 1

                if not stack:
                    countLeft += 1
                else:
                    stack.pop()

            else:
                stack.append(b)
            

        return countLeft + countRight + len(stack) * 2