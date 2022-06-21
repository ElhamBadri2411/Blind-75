class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        window_start = 0
        max_length = 0
        max_letter_count = 0
        
        
        
        for window_end in range(len(s)):
            r_char = s[window_end]
            
            if r_char not in lookup:
                lookup[r_char] = 0
            lookup[r_char] += 1
            
            max_letter_count = max(max_letter_count, lookup[r_char])
            
            if window_end - window_start + 1 - max_letter_count > k:
                l_char = s[window_start]
                lookup[l_char] -= 1
                window_start += 1
                
            max_length = max(max_length, window_end- window_start + 1)
            
        return max_length
            
            
        