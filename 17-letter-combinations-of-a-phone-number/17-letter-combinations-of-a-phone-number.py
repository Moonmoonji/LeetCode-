class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 17번 전화 번호 문자 조합 

        phone = {"2" : ['a','b','c'],"3" : ['d','e','f'],"4" : ['g','h','i'],"5" : ['j','k','l'],
                "6" : ['m','n','o'],"7" : ['p','q','r','s'],"8" : ['t','u','v'],"9" : ['w','x','y','z']} 

        def dfs(index,path) :
            if len(path) == len(digits):
                result.append(path)
                return 

            for i in range(index,len(digits)):
                for j in phone[digits[i]]:
                    dfs(i+1,path+j)
        
        if not digits : 
            return []
        result = []
        dfs(0,"")

        return result