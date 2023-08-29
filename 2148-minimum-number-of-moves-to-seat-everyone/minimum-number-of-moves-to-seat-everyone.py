class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n1 = len(seats)
        n2 = len(students)
        ans = []

        seats = sorted(seats)
        students = sorted(students)

        for i in range(0, n1):
            x = abs(seats[i] - students[i])  

            ans.append(x)

        tsum = sum(ans)

        return tsum      