class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_start = 0
        matches = 0
        substring_start = 0
        min_len = len(s) + 1
        lookup = {}
        
        for letter in t: # add all letters in the pattern string to a hashmap
            if letter not in lookup:
                lookup[letter] = 0
            lookup[letter] += 1
            
        for window_end in range(len(s)): # iterate through the string one letter at a time
            r_char = s[window_end]
            if r_char in lookup: # check if the letter is in the hashmap
                lookup[r_char] -= 1 # subtract the char in the lookup
                if lookup[r_char] >= 0: # increase the mathc count
                    matches += 1
            
            while matches == len(t): 
                # while the number of matches is equal to the number of letters in the patter string
                # i.e we count all the letters in the pattern string in the current substring
                
                if min_len > window_end - window_start + 1:
                    # changes the current min length to the len of current window if it is smaller
                    min_len = window_end - window_start + 1
                    # changes the start of the substring to the correct index
                    substring_start = window_start
        
                # decrements the counts of matches if we remove a character from the window
                l_char = s[window_start]
                window_start += 1
                
                if l_char in lookup:
                    if lookup[l_char] == 0:
                        matches -= 1
                    lookup[l_char] += 1
                
        if min_len > len(s):
            return ""
        return s[substring_start: substring_start + min_len]