class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        didict = {}

        for num in nums:
            if num in didict:
                didict[num] += 1
            else:
                didict[num] = 1
        
        for values in didict.values():
            if values != 1:
                return True

        return False
         