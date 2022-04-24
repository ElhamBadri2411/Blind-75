class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {}
        
        for i in range(len(nums)):
            if nums[i] in results:
                return [results[nums[i]],i]
            else:
                results[ target - nums[i]] = i
            
            
        return []