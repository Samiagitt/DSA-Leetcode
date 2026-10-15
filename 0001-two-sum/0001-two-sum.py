class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}
        n=len(nums)-1
        for i, val in enumerate(nums):
            diff=target-val
            if diff in map:
                return [map[diff],i]
            map[val]=i
        return
