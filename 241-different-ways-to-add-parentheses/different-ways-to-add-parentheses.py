class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)
        sign = '+-*'
        ans = []

        if expression.isdigit():
            return [int(expression)]

        for i in range(n):
            if expression[i] in sign:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for l in left:
                    for r in right:
                        if expression[i] == sign[0]:
                            ans.append(l + r)
                        elif expression[i] == sign[1]:
                            ans.append(l - r)
                        elif expression[i] == sign[2]:
                            ans.append(l * r)

        return ans