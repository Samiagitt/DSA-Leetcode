class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        prod = 1
        count = 0
        left = 0
        
        if k <= 1:
            return 0
        for r in range(len(nums)):
            prod *= nums[r]

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += r - left + 1

        return count
            
