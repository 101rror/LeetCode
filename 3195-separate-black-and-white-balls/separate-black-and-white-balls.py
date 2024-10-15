class Solution:
    def minimumSteps(self, s: str) -> int:
        swapcount = 0
        blackball = 0

        for col in s:
            if col == '0':
                swapcount += blackball
            else:
                blackball += 1

        return swapcount