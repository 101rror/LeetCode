from sortedcontainers import SortedList

class MyCalendarTwo:

    def __init__(self):
        self.lst = SortedList()

    def book(self, start: int, end: int) -> bool:
        self.lst.add((start, 1))
        self.lst.add((end, -1))

        count = 0

        for x, y in self.lst:
            count += y
            if count == 3:
                self.lst.remove((start, 1))
                self.lst.remove((end, -1))
                return False

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)