class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        array_nums = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0 :
                        array_nums.append([nums[i],nums[j],nums[k]])
        
        array_nums = [sorted(x) for x in array_nums]
        new_array =[ ]
        for x in array_nums :
            if x not in new_array :
                new_array.append(x)
        return new_array
        ''' 
        
        # Two Pointer 풀이 
        
        nums.sort()
        array_nums = [] 
        
        for i in range(len(nums)-2): 
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1 
            right = len(nums)-1
            
            while left<right : 
                sums = nums[i]+nums[right]+nums[left] 
                
                if sums == 0 : 
                    array_nums.append([nums[i],nums[left],nums[right]])
                    
                    # 동일한 값 있을 때 skip 
                    while left<right and nums[left] == nums[left+1] : 
                        left += 1 
                    
                    while left<right and nums[right] == nums[right-1]:
                        right -=1 
                    
                    left += 1 
                    right -= 1 
                
                elif sums < 0 : 
                    left += 1 
                
                else: 
                    right -= 1 
        
        return array_nums       
            
                    