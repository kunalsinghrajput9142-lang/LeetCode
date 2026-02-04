class Solution:
    def isHappy(self,n):
        seen=set()
        while n not in seen:
            seen.add(n)
            n=sum(int(d)**2 for d in str(n))
            if n==1:
                return True
        return False
