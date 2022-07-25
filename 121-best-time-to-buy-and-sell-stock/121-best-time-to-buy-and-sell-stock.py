class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_nums = 1000000 
        diff = 0 
        for i in range(len(prices)):
            if prices[i]< min_nums : 
                min_nums = prices[i] 

            if prices[i] - min_nums  == 0 : 
                continue 
            else : 
                if prices[i]-min_nums > diff: 
                    diff = prices[i] - min_nums 
        return diff