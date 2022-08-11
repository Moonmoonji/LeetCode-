class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections 
        
        nums = sorted(nums) 
        topk= collections.Counter(nums).most_common(k)

        la = [x[0] for x in topk]
        
        return la 