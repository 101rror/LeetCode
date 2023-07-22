class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap = []

        i = 0
        j = n - 1
        x = candidates
        
        while(i <= j and x > 0):
            heappush(heap, (costs[i], i))
            if (i != j):
                heappush(heap, (costs[j], j))
            i += 1
            j -= 1
            x -= 1
    
        total = 0
        for _ in range(k):
            c, ind = heappop(heap)
            total += c
        
            if (i <= j):
                if (ind < i):
                    heappush(heap, (costs[i], i))
                    i += 1
                else:
                    heappush(heap, (costs[j], j))
                    j -= 1

        return total
            
                        