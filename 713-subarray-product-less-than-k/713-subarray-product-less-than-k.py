class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if len(nums) <= 1:
            return 0 
        
        product = 1 
        arr_count = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            product *= nums[window_end]
            
            while product >= k and window_start <= window_end:
                product /= nums[window_start]
                window_start += 1
        
            arr_count += window_end - window_start + 1
        
        return arr_count
            
            
            
            
    
        