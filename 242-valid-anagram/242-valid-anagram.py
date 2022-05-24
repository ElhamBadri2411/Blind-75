class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup_s = {}
        lookup_t = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            lookup_s[s[i]] = lookup_s.get(s[i], 0) + 1
            lookup_t[t[i]] = lookup_t.get(t[i], 0) + 1
            
        for letter in lookup_s:
            if letter not in lookup_t or letter not in lookup_s or lookup_s[letter] != lookup_t[letter]:
                return False
    # n is length of s
    # O(n)
        
        return True