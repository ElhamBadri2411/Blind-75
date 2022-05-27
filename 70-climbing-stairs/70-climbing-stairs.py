class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: 
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2 
        dp_array = [0] * n
        dp_array[0] = 1
        dp_array[1] = 2
        for i in range(2, n):
            dp_array[i] = dp_array[i - 1] + dp_array[i - 2]
            
        return dp_array[n - 1]
        