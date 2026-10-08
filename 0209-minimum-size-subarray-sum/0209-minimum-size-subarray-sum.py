class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n=len(nums)
        l=0
        sum=0
        min_len=(float('inf'))
        for r in range(n):
            sum+=nums[r]
            while(sum>=target):
                min_len=min(min_len,r-l+1)
                sum-=nums[l]
                l=l+1
        return 0 if min_len==float('inf') else min_len