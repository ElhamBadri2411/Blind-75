class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1
        
        while l < r:
            if s[l] != s[r]:
                skipFirst = s[l + 1: r + 1]
                skipLast = s[l: r]

                return self.isPalindrome(skipFirst) or self.isPalindrome(skipLast)
            
            l = l + 1
            r = r - 1
            
        return True
            
    def isPalindrome(self, s):
        return s == s[::-1]
        