class Solution:
 def reverseDigits(self, n):
  sr=""
  num=str(n)
  for i in range(len(num)-1,-1,-1):
      sr+=num[i]
  return int(sr)
		    