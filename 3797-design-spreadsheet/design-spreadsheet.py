class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.spreadsheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.spreadsheet[cell] = 0

    def getValue(self, formula: str) -> int:
        left, right = formula[1:].split("+")
        x = int(left) if left.isdigit() else self.spreadsheet[left]
        y = int(right) if right.isdigit() else self.spreadsheet[right]
        
        return x + y


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
