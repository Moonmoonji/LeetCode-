class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = [] 
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target : 
                    answer.append([i,j])
                    break 
                    break
            
        return answer[0]