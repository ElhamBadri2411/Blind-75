class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lookup = {}
        window_start = 0
        matches = 0
        result_indices = []
        
        for letter in p:
            if letter not in lookup:
                lookup[letter] = 0
            lookup[letter] += 1
        
        for window_end in range(len(s)):
            r_char = s[window_end]
            if r_char in lookup:
                lookup[r_char] -= 1
                if lookup[r_char] == 0:
                    matches += 1
            
            if matches == len(lookup):
                result_indices.append(window_start)
                
            if window_end >= len(p) - 1:
                l_char = s[window_start]
                window_start += 1
                if l_char in lookup:
                    if lookup[l_char] == 0:
                        matches -= 1
                    lookup[l_char] += 1
                    
        return result_indices
                