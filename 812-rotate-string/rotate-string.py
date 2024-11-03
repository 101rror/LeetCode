class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 

        new = s + s

        if new.find(goal) != -1:
            return True

        return False