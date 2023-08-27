class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        null = moves.count("_")
        left = moves.count("L")
        right = moves.count("R")
        ans = null + abs(left - right)
                
        return ans
        