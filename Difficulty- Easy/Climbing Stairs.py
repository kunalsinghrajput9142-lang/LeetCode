class Solution:
    def climbStairs(self,steps):
        if steps<=2:
            return steps
        a,b=1,2
        for _ in range(3,steps+1):
            a,b=b,a+b
        return b    
