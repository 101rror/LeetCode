class Solution:
    def trimMean(self, arr: List[int]) -> float:
      arr = sorted(arr)
      n = len(arr)
      per = ((n * 5) // 100)
      ans = []
      

      for i in range(per, n - per):
        ans.append(arr[i])

      ln = len(ans)
      tsum = sum(ans)

      res = tsum / ln

      return res
      