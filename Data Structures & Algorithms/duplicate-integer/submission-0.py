class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for t in range(1,len(nums)):
            if nums[t] == nums[t-1]:
                return True
            
        return False
