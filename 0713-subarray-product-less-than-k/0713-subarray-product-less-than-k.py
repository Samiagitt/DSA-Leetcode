class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n=len(nums)
        l=0
        prod=1
        count=0
        if k<=1:
            return 0
        for r in range(n):
            prod=prod*nums[r]
            while(prod>=k):
                prod/=nums[l]
                l=l+1
            count+=r-l+1
        return count
            
