class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0

        for val in operations:
            if val == "++X" or val == "X++":
                ans += 1
            else:
                ans -= 1

        return ans
