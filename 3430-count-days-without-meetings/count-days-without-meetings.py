class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        check = []
        count = 0

        for meeting in meetings:
            if not check or meeting[0] > check[-1][1]:
                check.append(meeting)
            else:
                check[-1][1] = max(check[-1][1], meeting[1])

        for start, end in check:
            count += end - start + 1

        return days - count
