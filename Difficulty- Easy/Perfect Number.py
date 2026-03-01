class Solution:
    def checkPerfectNumber(self,num):
        return num>1 and sum(i+(num//i if i*i!=num else 0)
                               for i in range(2,int(num**0.5)+1)
                               if num%i==0)+1==num
                               