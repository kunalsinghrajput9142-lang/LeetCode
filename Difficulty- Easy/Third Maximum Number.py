class Solution:
    def thirdMax(self,nums):
        nums=sorted(set(nums),reverse=True)
        return nums[2] if len(nums)>2 else nums[0]
