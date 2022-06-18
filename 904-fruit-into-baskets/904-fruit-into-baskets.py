class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        lookup = {}
        window_start = 0
        max_length = 0
        
        for i in range(len(fruits)):
            right_tree = fruits[i]
            if right_tree not in lookup:
                lookup[right_tree] = 0
            lookup[right_tree] += 1
            
            while len(lookup) > 2: # Check and remove count
                left_tree = fruits[window_start]
                lookup[left_tree] -= 1
                if lookup[left_tree] == 0:
                    del lookup[left_tree]
                window_start += 1
            
            
            max_length = max(max_length, i - window_start + 1)
        
        
        return max_length
            
            
        