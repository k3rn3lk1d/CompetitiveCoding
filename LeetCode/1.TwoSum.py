class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            reminder = target - nums[i]
            if reminder in dic:
                return [dic[reminder],i]
            dic[nums[i]] = i
            
