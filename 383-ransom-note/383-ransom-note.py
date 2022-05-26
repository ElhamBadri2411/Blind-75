class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCount = {}
        magazineCount = {}
        for letter in ransomNote:
            ransomCount[letter] = ransomCount.get(letter, 0) + 1
            
        for letter in magazine:
            magazineCount[letter] = magazineCount.get(letter, 0) + 1
            
        for letter in ransomCount:
            if letter not in magazineCount or ransomCount[letter] > magazineCount[letter]:
                return False
            
            
        return True