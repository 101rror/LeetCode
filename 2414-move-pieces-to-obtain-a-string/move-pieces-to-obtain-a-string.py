class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False

        i = j = 0
        n = len(start)

        while i < n and j < n:
            while i < n and start[i] == "_":
                i += 1
            while j < n and target[j] == "_":
                j += 1
            if ( i < n and j < n and (start[i] == "L" and i < j or start[i] == "R" and i > j)):
                return False

            i += 1
            j += 1
            
        return True
