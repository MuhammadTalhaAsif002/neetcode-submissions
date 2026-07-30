class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        suff_prod=1
        pre_prod=1
        size=len(nums)
        for i in range(size):
            res.append(suff_prod)
            suff_prod*=nums[i]
        for i in range(size-1,-1,-1):
            res[i] *=pre_prod
            pre_prod*=nums[i]
        return res
        

