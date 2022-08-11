import collections 

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        sums = 0 
        for i in jewels : 
            sums += freq[i] 
        
        return sums 