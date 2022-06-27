class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) == 1 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key = len)

        return result
        '''
        if len(s) == 1 or  s == s[::-1]: 
            longest_palindrome = s 
            
        else : 
            longest_palindrome = s[0]
            for i in range(len(s)):
                for j in range(1,len(s)+1):
                    if len(longest_palindrome) >= len(s[i:j]):
                        continue
                    
                    if s[i:j]==s[i:j][::-1] :
                        longest_palindrome = s[i:j]
                          
        return longest_palindrome
        ''' 
    