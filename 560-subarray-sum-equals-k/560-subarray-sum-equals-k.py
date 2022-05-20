class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        res = 0
        premap = {0 : 1}
        
        for n in nums:
            curr_sum += n
            
            curr_diff = curr_sum - k
            
            res += premap.get(curr_diff, 0)
            premap[curr_sum] = premap.get(curr_sum, 0) + 1
            
        return res
            