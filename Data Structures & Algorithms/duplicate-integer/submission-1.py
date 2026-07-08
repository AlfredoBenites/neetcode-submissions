class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 0

        for num in range(1, len(nums)):
            if nums[num] == nums[i]:
                return True
            else:
                i += 1

        return False
         