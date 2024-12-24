class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def getDiameter(edges):
            mp = defaultdict(list)
            for i, j in edges:
                mp[i].append(j)
                mp[j].append(i)
            
            res = [0]
            
            def dfs(node, parent):
                mx = 1
                for ng in mp[node]:
                    if ng == parent:
                        continue
                    depth = dfs(ng, node)
                    res[0] = max(res[0], mx + depth)
                    mx = max(mx, 1 + depth)
                return mx
            
            dfs(0, -1)
            
            return res[0]
        
        d1 = getDiameter(edges1)
        d2 = getDiameter(edges2)
        
        return max(d1 - 1, d2 - 1, d1 // 2 + d2 // 2 + 1)