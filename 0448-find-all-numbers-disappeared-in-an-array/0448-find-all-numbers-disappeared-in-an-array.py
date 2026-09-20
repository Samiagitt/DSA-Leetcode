class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return_arr=[]
        set_nums=set(nums)

        for i in range (1, len(nums)+1):
            if i not in set_nums:
                return_arr.append(i)

        return return_arr
        