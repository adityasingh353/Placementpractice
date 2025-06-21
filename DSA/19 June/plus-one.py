class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sr=""
        lst=[]
        for i in digits:
            sr+=str(i)
        a=str(int(sr)+1)
        for i in range(0,len(a)):
            lst.append(int(a[i]))
        return lst
        
        
        
            
        