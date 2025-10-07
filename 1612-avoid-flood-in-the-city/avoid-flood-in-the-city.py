class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        freq = {}
        q = deque()
        ans = []

        for i, rain in enumerate(rains):
            if rain:
                if rain in freq:
                    for j in q:
                        if j > freq[rain]:
                            ans[j] = rain
                            q.remove(j)
                            break
                    else:
                        return []
                ans.append(-1)
                freq[rain] = i
            else:
                ans.append(1)
                q.append(i)

        return ans
