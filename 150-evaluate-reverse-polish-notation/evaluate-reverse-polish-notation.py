class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
      
        for i in tokens:
            if len(i) > 1 or i.isdigit():
                stack.append(int(i))
            else:
                if i == "+":
                    stack[-2] += stack[-1]
                elif i == "-":
                    stack[-2] -= stack[-1]
                elif i == "*":
                    stack[-2] *= stack[-1]
                else:
                    stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
      
        return stack[0]