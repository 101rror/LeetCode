class NumberContainers:
    def __init__(self):
        self.index_val = {}
        self.ans = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_val:
            prevNum = self.index_val[index]
            if prevNum == number:
                return

        self.index_val[index] = number

        if number not in self.ans:
            self.ans[number] = []
        heapq.heappush(self.ans[number], index)

    def find(self, number: int) -> int:
        if number not in self.ans:
            return -1

        while self.ans[number] and self.index_val[self.ans[number][0]] != number:
            heapq.heappop(self.ans[number])

        return self.ans[number][0] if self.ans[number] else -1
