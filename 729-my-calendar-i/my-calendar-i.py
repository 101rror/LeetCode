class MyCalendar:
    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        for st, en in self.calender:
            if st < end and en > start:
                return False

        self.calender.append((start, end))

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)