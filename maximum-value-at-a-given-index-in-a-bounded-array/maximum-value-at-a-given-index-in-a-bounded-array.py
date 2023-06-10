class Solution:
    def maxValue(self, n, index, maxSum):
        maxSum -= n
        first, last = 0, maxSum

        while(first != last):
            m = (first + last + 1) // 2
            
            s = max(0, m - index - 1)
            e = max(0, m - n + index)

            if(m * m <= maxSum + (s * (s + 1) + e * (e + 1)) // 2):
                first = m
            else:
                last = m - 1

        ans = last + 1
        
        return ans