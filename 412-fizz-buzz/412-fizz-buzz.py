class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        soln = []
        
        for i in range(1,n+1):
            if  i % 5 == 0 and i % 3 == 0:
                soln.append("FizzBuzz")
            elif i % 5 == 0:
                soln.append("Buzz")
            elif i % 3 == 0:
                soln.append("Fizz")
            else:
                i = str(i)
                soln.append(i)
                
        return soln
        