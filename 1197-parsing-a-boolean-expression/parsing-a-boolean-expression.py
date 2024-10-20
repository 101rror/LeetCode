class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        def OR(stack):
            for s in stack:
                if s == 't':
                    return 't'
            return 'f'

        def AND(stack):
            for s in stack:
                if s == 'f':
                    return 'f'
            return 't'

        def NOT(stack):
            if stack[0] == 'f':
                return 't'
            else:
                return 'f'

        for char in expression:
            if char == ',':
                continue
            if char == ')':
                tempstack = []
                top = stack.pop()

                while top != '(':
                    tempstack.append(top)
                    top = stack.pop()

                top = stack.pop()

                if top == '|':
                    stack.append(OR(tempstack))
                if top == '&':
                    stack.append(AND(tempstack))
                if top == '!':
                    stack.append(NOT(tempstack))

            else:
                stack.append(char)

        return 't' in stack