class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0]) == 0:
            return []
        
        
        word_lookup = {}
        
        for word in words:
            if word not in word_lookup:
                word_lookup[word] = 0
            word_lookup[word] += 1
            
        result = []
        num_words = len(words)
        word_len = len(words[0])
        
        for i in range (len(s) - num_words * word_len + 1):
            words_seen = {}
            for j in range (0, num_words):
                word_index = j * word_len + i
                word = s[word_index: word_index + word_len]
                
                if word not in word_lookup:
                    break
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                if words_seen[word] > word_lookup.get(word, 0):
                    break
                if j + 1 == num_words:
                    result.append(i)

        return result