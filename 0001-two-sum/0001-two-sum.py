class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i, value in enumerate(nums):
            diff=target-value
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[value]=i
        return
        