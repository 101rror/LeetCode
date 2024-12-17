class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counter = Counter(s)
        heap = [(-ord(key), val) for key, val in counter.items()] 
        heapify(heap)
        ans = []

        while heap:
            key, val = heappop(heap)
            char = chr(-key)

            if val <= repeatLimit:
                ans.append(char * val)
            else:
                ans.append(char * repeatLimit)
                
                if not heap:
                    break

                nextkey, nextval = heappop(heap)
                nextchar = chr(-nextkey)
                ans.append(nextchar)

                if nextval > 1:
                    heapq.heappush(heap, (nextkey, nextval - 1))

                heapq.heappush(heap, (key, val - repeatLimit))

        return ''.join(ans)