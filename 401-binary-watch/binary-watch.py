class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []

        for hour in range(12):
            for mint in range(60):
                if (bin(hour).count("1") + bin(mint).count("1")) == turnedOn:
                    time = f"{hour}:{mint:02}"
                    ans.append(time)

        return ans
