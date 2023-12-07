class Solution:
  def largestOddNumber(self, num: str) -> str:
    while(True):
      if(len(num) < 1 or (int(num[-1]) % 2) == 1):
        return num
      num = num[:-1]