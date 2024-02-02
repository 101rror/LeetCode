class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        num = "123456789"
        n = len(num)
        ans = []

        for i in range(n):
            for j in range(i + 1, n):
                c = int(num[i : j + 1])

                if(c >= low and c <= high):
                    ans.append(c)

        ans.sort()
        return ans
            