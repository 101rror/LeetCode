class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            drop = len(row) - 1  
            
            for cur in range(len(row) - 1, -1, -1):
                if row[cur] == "*":  
                    drop = cur - 1
                elif row[cur] == "#":  
                    row[drop], row[cur] = row[cur], row[drop]
                    drop -= 1

        ans = zip(*box[::-1])

        return ans