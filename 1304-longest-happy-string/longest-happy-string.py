class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counter = Counter({'a':a, 'b':b, 'c':c})
        ans = ''

        while True:
            (a1, _), (a2, _) = counter.most_common(2)
            
            if len(ans) >= 2 and ans[-1] == ans[-2] == a1:
                a1 = a2
                
            if not counter[a1]:
                break
                
            ans += a1
            counter[a1] -= 1            
        
        return ans 