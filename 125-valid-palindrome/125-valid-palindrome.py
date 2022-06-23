class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s : 
            if char.isalnum():
                strs.append(char.lower()) 
        
        start = 0 
        end = len(strs)-1
        
        while start < end : 
            if strs[start] == strs[end]: 
                start += 1
                end -= 1 
                
            else : 
                return False
        
        return True 