class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0] * (n + 1)
        count = 0
        
        for i in range(n):
            pre[i + 1] = pre[i] ^ arr[i]
        
        for i in range(n):
            for k in range(i + 1, n):
                if pre[i] == pre[k + 1]:
                    count += (k - i)
        
        return count