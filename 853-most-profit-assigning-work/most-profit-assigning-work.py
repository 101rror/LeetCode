class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        res, j, count, lst = 0, 0, 0, []
        
        for i in range(len(worker)):
            lst.append((difficulty[i], profit[i]))
        
        lst.sort()
        worker.sort()
        
        for work in worker:
            while j < len(lst) and work >= lst[j][0]:
                count = max(count, lst[j][1])
                j += 1
            
            res += count
        
        return res