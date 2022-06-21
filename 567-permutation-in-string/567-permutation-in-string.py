class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        matches = 0
        lookup = {}
        
        for letter in s1:
            if letter not in lookup:
                lookup[letter] = 0
            lookup[letter] += 1
            
            
            
        for window_end in range(len(s2)):
            r_char = s2[window_end]
            
            if r_char in lookup:
                lookup[r_char] -= 1
                if lookup[r_char] == 0:
                    matches += 1
                
            if matches == len(lookup):
                return True
            
            
            
            if window_end >= len(s1) - 1:
                l_char = s2[window_start]
                window_start += 1
                
                if l_char in lookup:
                    if lookup[l_char] == 0:
                        matches -= 1
                    lookup[l_char] += 1
                    
        return False
        


                
            