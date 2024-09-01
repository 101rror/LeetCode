class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ln = len(original)
        ans = []

        if ln == m * n: 
            for i in range(0, ln, n): 
                ans.append(original[i : i + n])
                
        return ans 