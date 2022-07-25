class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums) 
        ret = []
        for i in range(0,len(nums),2):
            ret.append(min(nums[i],nums[i+1]))
        
        return sum(ret)