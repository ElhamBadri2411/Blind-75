class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        
        lookup = {}
        
        for letter in s:
            lookup[letter] = lookup.get(letter, 0) + 1
            
        #can only have one odd nuber of letter
        odd_found = False
        palindrome_len = 0 
        
        for letter in lookup:
            if lookup[letter] % 2 == 1:
                
                if not odd_found:
                    odd_found = True
                    palindrome_len += 1
                
                if lookup[letter] // 2 > 0:
                    palindrome_len += (lookup[letter] // 2) * 2
                     
            else:
                palindrome_len += lookup[letter]
           
        return palindrome_len