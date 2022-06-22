class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = 0
        matches = 0
        lookup = {}
        
        #Add all the letters in the s1 string to a hashmap
        for letter in s1: 
            if letter not in lookup:
                lookup[letter] = 0
            lookup[letter] += 1
            
        #Incrementing the window            
        for window_end in range(len(s2)):
            r_char = s2[window_end]
            
            if r_char in lookup: # if the character is in the s1 lookup
                lookup[r_char] -= 1 # we reduce the count of the letter
                if lookup[r_char] == 0: # if the lookup hits 0, increase the number of matches by one
                    matches += 1
                
            if matches == len(lookup): # check if the matches is equal to the number of unique numbers
                return True
            
            
            
            if window_end >= len(s1) - 1: #if the window_end index is larger than the max len, we decrement the start 
                l_char = s2[window_start]
                window_start += 1
                
                if l_char in lookup:
                    if lookup[l_char] == 0:
                        matches -= 1
                    lookup[l_char] += 1
                    
        return False
        


                
            