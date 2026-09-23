class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sort_nums=sorted(nums)
        d={}
        result=[]

        for i,value in enumerate(sort_nums):
            if value not in d:
                d[value]=i

        for i in nums:
            result.append(d[i])


        return result
        