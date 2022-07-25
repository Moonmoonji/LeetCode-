class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [] 
        m = 1 
        
        for i in range(len(nums)):
            left.append(m)
            m *= nums[i] 
        
        m = 1
        right = []
        
        for i in range(len(nums)-1,-1,-1) : 
            right.insert(0,m) 
            m*=nums[i] 
            
        ret = []
        '''
        1,1,2,6
        24,12,4,1
        ''' 
        
        for i in range(len(nums)):
            ret.append(left[i]*right[i])
        return ret