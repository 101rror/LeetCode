class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime = sorted(processorTime)
        tasks = sorted(tasks, reverse = True)
        c = []
        ans = 0
        
        for i in processorTime:
            c.append(i)
            c.append(i)
            c.append(i)
            c.append(i)
        
        for i in range(0, len(tasks)):
            x = (tasks[i] + c[i])
            
            ans = max(ans, x)
                        
        return ans
        
            