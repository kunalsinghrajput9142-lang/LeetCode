class Solution:
    def romanToInt(self,s):
        r={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        n=len(s)
        i=0
        while i<n:
            if i<n-1 and r[s[i]]<r[s[i+1]]:
                total+=r[s[i+1]]-r[s[i]]
                i+=2
            else:
                total+=r[s[i]]
                i+=1 
        return total              