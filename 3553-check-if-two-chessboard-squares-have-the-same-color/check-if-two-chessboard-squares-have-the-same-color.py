class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x = ord(coordinate1[0]) - 96
        x1 = int(coordinate1[1])
        y =  ord(coordinate2[0]) - 96
        y1 = int(coordinate2[1])

        if (abs(x - x1) & 1 and abs(y - y1) & 1) or (abs(x - x1) % 2 == 0 and abs(y - y1) % 2 == 0):
            return True
        else:
            return False