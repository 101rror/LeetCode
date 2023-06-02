class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def is_connected(a,b):
            x1, y1, r1 = bombs[a]
            x2, y2, r2 = bombs[b]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            return dist <= r1

        conn = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if (i != j):
                    if (is_connected(i,j)):
                        conn[i].append(j)             
                    
        def dfs(node):
            if(node in visited):
                return 0

            visited.add(node)
            ans = 1
            if (node in conn):
                for child in conn[node]:
                    if (child in visited):
                        continue
                    ans += dfs(child)
            
            return ans 

        maxRes = 1
        for node in conn:
            visited = set()
            maxRes = max(maxRes, dfs(node))

        return maxRes