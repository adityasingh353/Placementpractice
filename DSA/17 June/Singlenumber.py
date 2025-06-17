class Solution(object):
    def singleNumber(self, nums):
        ls=set(nums)
        for i in ls:
            if nums.count(i)==1:
                return i
                