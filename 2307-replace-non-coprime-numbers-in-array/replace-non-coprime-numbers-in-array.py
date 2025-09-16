class Solution(object):
    def replaceNonCoprimes(self, nums):
        stack = []

        for num in nums:
            while stack:
                lcm = gcd(stack[-1], num)
                if lcm == 1:
                    break
                num = (stack.pop() * num) // lcm

            stack.append(num)

        return stack
