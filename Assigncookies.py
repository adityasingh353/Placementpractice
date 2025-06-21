class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        cnt = 0
        g.sort()
        s.sort()
        cnt=0
        i=0
        j=0
        while i<=(len(g)-1) and j<=(len(s)-1):
            if g[i]<=s[j]:
                i+=1
                j+=1
                cnt+=1
            elif i!=(len(g)-1) or j!=(len(s)-1):
                j+=1
        return cnt
                


 
        
        