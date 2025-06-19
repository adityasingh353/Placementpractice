class Solution(object):
    def maxProfit(self, prices):
        b=prices[0]
        prof=0
        for i in prices:
            if i<b:
                b=i
            elif i-b>prof:
                prof=i-b
        return prof
        