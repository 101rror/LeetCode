class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        fSum = 0

        for num in nums:
            div = []
            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    div.append(i)
                    if i != num // i:
                        div.append(num // i)

            if len(div) == 4:
                fSum += sum(div)

        return fSum
