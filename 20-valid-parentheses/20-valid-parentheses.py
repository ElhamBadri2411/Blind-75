class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:          
            if c == '(' or c == '{' or c =='[': # if its an opening bracket we add it to the stacj
                stack.append(c)
            else:
                if not stack: # if the stack is empty at this point and we have a closing bracket, its not correct
                    return False
                
                # check the stack if closing bracket corresponds with opening
                if c == ')' and stack[-1] == '(': 
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:   # check if the stack is empty     
            return True 
        
        return False        
                    
                
                
        