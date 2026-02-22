class Solution:
    def longestCommonPrefix(self,strs):
        strs.sort()
        first,last=strs[0],strs[-1]
        i=0
        while i<len(first) and first[i]==last[i]:
            i+=1
        return first[:i]    
