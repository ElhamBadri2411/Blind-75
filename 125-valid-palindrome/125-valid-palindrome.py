class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for letter in s:
            if letter.isalnum():
                new_s += letter
                
 
 
        if new_s.lower() == new_s[::-1].lower():
            return True
        
        return False
                
        
        