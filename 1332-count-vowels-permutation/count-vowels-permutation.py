class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = (10**9) + 7
        a, e, i1, o, u = 1, 1, 1, 1, 1

        for i in range(2, n + 1):
            a2 = e
            e2 = a + i1
            i2 = a + e + o + u 
            o2 = i1 + u
            u2 = a

            a, e, i1, o, u = a2, e2, i2, o2, u2
        
        ans = a + e + i1 + o + u
       
        return (ans) % MOD

        
        