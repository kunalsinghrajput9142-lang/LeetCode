class Solution:
    def searchInsert(self,nums,target):
        l=0
        r=len(nums)-1
        while l<=r:
            p=(l+r)//2
            if nums[p]<target:
                l=p+1
            elif nums[p]>target:
                r=p-1
            else:
                return p
        return l
