#User function Template for python3

class Solution:
    def findSingle(self, arr):
        res=0
        for i in arr:
            res^=i
        return res