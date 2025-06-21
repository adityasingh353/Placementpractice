class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        ma=nums[0]
        for i in nums:
            sum=sum+i
            ma=max(ma,sum)
            if sum<0:
                sum=0
        return ma