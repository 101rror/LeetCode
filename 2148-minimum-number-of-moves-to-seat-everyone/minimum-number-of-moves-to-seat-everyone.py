class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        n = len(seats)
        tsum = 0

        seats = sorted(seats)
        students = sorted(students)

        for i in range(0, n):
            tsum += abs(seats[i] - students[i])  

        return tsum      