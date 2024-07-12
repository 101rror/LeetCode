class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'ab', 'ba'
        if y > x:
            b, a, y, x = a, b, x, y

        ans = 0
        
        for word in [a, b]:
            stack = []

            i = 0
            while i < len(s):
                stack.append(s[i])
                
                n = len(stack)
                pre = stack[n - 2] + stack[n - 1]

                if pre == word:
                    ans += x
                    stack.pop()
                    stack.pop()
                i += 1

            x = y
            
            s = ''.join(stack)

        return ans