class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        max_len = 0
        window_start = 0
        
        for window_end in range(len(nums)):
            r_num = nums[window_end]
            
            if r_num == 1:
                max_ones += 1
            
            if window_end - window_start + 1 - max_ones > k:
                if nums[window_start] == 1:
                    max_ones -= 1
                window_start += 1
                
            max_len = max(max_len, window_end - window_start + 1)
            
        return max_len