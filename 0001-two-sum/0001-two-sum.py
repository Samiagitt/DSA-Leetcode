class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 1. Sort the numbers normally
        sorted_nums = sorted(nums)
        
        # 2. Your exact two-pointer code
        left = 0
        right = len(nums) - 1

        while left < right:
            curr_sum = sorted_nums[left] + sorted_nums[right]
            
            if curr_sum == target:
                # 3. Find the original indices simply
                idx1 = nums.index(sorted_nums[left])
                
                # Temporarily "erase" the first number so .index() won't see it again
                nums[idx1] = None 
                
                # Now finding the second number is perfectly safe, even if it's a duplicate!
                idx2 = nums.index(sorted_nums[right])
                
                return [idx1, idx2]
                
            elif curr_sum > target:
                right = right - 1
            else:
                left = left + 1
                
        return []